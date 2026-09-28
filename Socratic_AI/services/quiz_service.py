import uuid
import json
from typing import List, Dict, Any, Optional
from app.config import settings
from app.database import get_db
from app.schema import (
    QuizSet, QuizQuestion, QuizSubmitRequest, 
    QuizFeedback, QuizResultItem, MasterySummary, MasteryMetric
)
from app.prompts import ADAPTIVE_QUIZ_PROMPT, ADAPTIVE_QUIZ_TOPIC_PROMPT
from services.rag_service import rag_service

class QuizService:
    def __init__(self):
        pass

    def _get_student_difficulty(self, source_id: str) -> str:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT AVG(score) as avg_score FROM mastery_scores WHERE document_id = ?",
                (source_id,)
            )
            row = cursor.fetchone()
            avg_score = row["avg_score"] if row and row["avg_score"] is not None else 0.0

        if avg_score < 0.5:
            return "Beginner"
        elif avg_score < 0.8:
            return "Intermediate"
        else:
            return "Advanced"

    def generate_quiz(
        self,
        document_id: Optional[str] = None,
        topic_name: Optional[str] = None,
        num_questions: int = 5,
        api_key: Optional[str] = None,
    ) -> QuizSet:
        source_id = document_id or topic_name or "general"
        difficulty = self._get_student_difficulty(source_id)

        if document_id:
            chunks = rag_service.get_relevant_chunks(document_id, query="", top_k=6, api_key=api_key)
            context_str = "\n---\n".join(chunks)
            prompt = ADAPTIVE_QUIZ_PROMPT.format(
                num_questions=num_questions,
                difficulty=difficulty,
                context=context_str
            )
        elif topic_name:
            prompt = ADAPTIVE_QUIZ_TOPIC_PROMPT.format(
                num_questions=num_questions,
                topic_name=topic_name,
                difficulty=difficulty
            )
        else:
            prompt = ADAPTIVE_QUIZ_TOPIC_PROMPT.format(
                num_questions=num_questions,
                topic_name="General Knowledge",
                difficulty=difficulty
            )

        resolved_gemini_key = settings.get_api_key("quiz", api_key)

        if resolved_gemini_key:
            try:
                from google import genai
                from google.genai import types

                client = genai.Client(api_key=resolved_gemini_key)

                response = client.models.generate_content(
                    model=settings.MODEL_NAME,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=QuizSet,
                        temperature=0.3,
                    )
                )

                quiz_set = QuizSet.model_validate_json(response.text)
                self._save_quiz_questions(source_id, quiz_set.questions)
                return quiz_set
            except Exception as e:
                print(f"[QuizService] Error using Gemini API: {e}")

        title = topic_name or "Document Notes"
        fallback_questions = []
        for idx in range(num_questions):
            q_id = str(uuid.uuid4())
            concept = f"Core Principle {idx+1}"
            correct_opt = f"Correct answer statement for {concept} in {title}"
            options = [
                correct_opt,
                f"Incorrect distractor 1 for {concept}",
                f"Incorrect distractor 2 for {concept}",
                "None of the above"
            ]

            question = QuizQuestion(
                id=q_id,
                question_text=f"Regarding '{title}', which statement is true about {concept}?",
                options=options,
                correct_answer=correct_opt,
                explanation=f"Key theoretical rule for {concept} in {title}.",
                concept=concept,
                difficulty=difficulty
            )
            fallback_questions.append(question)

        quiz_set = QuizSet(topic=f"{title} Quiz ({difficulty})", questions=fallback_questions)
        self._save_quiz_questions(source_id, quiz_set.questions)
        return quiz_set

    def _save_quiz_questions(self, source_id: str, questions: List[QuizQuestion]):
        with get_db() as conn:
            cursor = conn.cursor()
            for q in questions:
                cursor.execute(
                    """
                    INSERT OR REPLACE INTO quiz_questions 
                    (id, document_id, question_text, options_json, correct_answer, explanation, concept, difficulty) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        q.id, source_id, q.question_text, json.dumps(q.options),
                        q.correct_answer, q.explanation, q.concept, q.difficulty
                    )
                )
            conn.commit()

    def submit_quiz(self, payload: QuizSubmitRequest) -> QuizFeedback:
        source_id = payload.document_id or payload.topic_name or "general"
        results = []
        correct_count = 0
        total = len(payload.answers)

        with get_db() as conn:
            cursor = conn.cursor()

            for ans in payload.answers:
                cursor.execute(
                    "SELECT * FROM quiz_questions WHERE id = ?",
                    (ans.question_id,)
                )
                row = cursor.fetchone()

                if not row:
                    continue

                q_text = row["question_text"]
                correct = row["correct_answer"]
                explanation = row["explanation"]
                concept = row["concept"]
                
                is_correct = (ans.selected_option.strip().lower() == correct.strip().lower())
                if is_correct:
                    correct_count += 1

                results.append(
                    QuizResultItem(
                        question_id=ans.question_id,
                        question_text=q_text,
                        user_answer=ans.selected_option,
                        correct_answer=correct,
                        is_correct=is_correct,
                        explanation=explanation,
                        concept=concept
                    )
                )

                cursor.execute(
                    "SELECT score, attempts FROM mastery_scores WHERE document_id = ? AND concept = ?",
                    (source_id, concept)
                )
                m_row = cursor.fetchone()
                
                new_score = 1.0 if is_correct else 0.0
                if m_row:
                    old_score = m_row["score"]
                    attempts = m_row["attempts"] + 1
                    updated_score = (old_score * 0.6) + (new_score * 0.4)
                    cursor.execute(
                        "UPDATE mastery_scores SET score = ?, attempts = ?, last_updated = CURRENT_TIMESTAMP WHERE document_id = ? AND concept = ?",
                        (updated_score, attempts, source_id, concept)
                    )
                else:
                    cursor.execute(
                        "INSERT INTO mastery_scores (document_id, concept, score, attempts) VALUES (?, ?, ?, 1)",
                        (source_id, concept, new_score)
                    )
            conn.commit()

        percentage = (correct_count / total * 100) if total > 0 else 0.0
        return QuizFeedback(
            total_questions=total,
            score=correct_count,
            percentage=round(percentage, 1),
            results=results
        )

    def get_mastery_summary(self, source_id: str) -> MasterySummary:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT concept, score, attempts FROM mastery_scores WHERE document_id = ?",
                (source_id,)
            )
            rows = cursor.fetchall()

        metrics = [
            MasteryMetric(concept=row["concept"], score=round(row["score"], 2), attempts=row["attempts"])
            for row in rows
        ]
        return MasterySummary(source_identifier=source_id, mastery_metrics=metrics)

quiz_service = QuizService()
