import uuid
from typing import List, Optional
from app.config import settings
from app.database import get_db
from app.schema import FlashcardSet, FlashcardItem
from app.prompts import FLASHCARD_GENERATION_PROMPT, FLASHCARD_TOPIC_PROMPT
from services.rag_service import rag_service

class FlashcardService:
    def __init__(self):
        pass

    def generate_flashcards(
        self,
        document_id: Optional[str] = None,
        topic_name: Optional[str] = None,
        num_cards: int = 5,
        api_key: Optional[str] = None,
        cerebras_key: Optional[str] = None,
        provider: Optional[str] = None
    ) -> FlashcardSet:
        source_id = document_id or topic_name or "general"

        if document_id:
            chunks = rag_service.get_relevant_chunks(document_id, query="", top_k=6, api_key=api_key)
            context_str = "\n---\n".join(chunks)
            prompt = FLASHCARD_GENERATION_PROMPT.format(num_cards=num_cards, context=context_str)
        elif topic_name:
            prompt = FLASHCARD_TOPIC_PROMPT.format(num_cards=num_cards, topic_name=topic_name)
        else:
            prompt = FLASHCARD_TOPIC_PROMPT.format(num_cards=num_cards, topic_name="General Knowledge")

        resolved_gemini_key = settings.get_api_key("flashcard", api_key)

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
                        response_schema=FlashcardSet,
                        temperature=0.3,
                    )
                )

                flashcard_set = FlashcardSet.model_validate_json(response.text)
                self._save_flashcards(source_id, flashcard_set.cards)
                return flashcard_set
            except Exception as e:
                print(f"[FlashcardService] Error using Gemini API: {e}")

        t_title = topic_name or "Document Notes"
        fallback_cards = [
            FlashcardItem(
                front=f"What is a core concept of '{t_title}' (Card {i+1})?",
                back=f"Essential definition and key mechanism for card {i+1} in {t_title}.",
                explanation=f"Foundational study concept for {t_title}."
            )
            for i in range(num_cards)
        ]

        flashcard_set = FlashcardSet(cards=fallback_cards)
        self._save_flashcards(source_id, flashcard_set.cards)
        return flashcard_set

    def _save_flashcards(self, source_id: str, cards: List[FlashcardItem]):
        with get_db() as conn:
            cursor = conn.cursor()
            for card in cards:
                card_id = str(uuid.uuid4())
                cursor.execute(
                    "INSERT INTO flashcards (id, document_id, front, back, explanation) VALUES (?, ?, ?, ?, ?)",
                    (card_id, source_id, card.front, card.back, card.explanation)
                )
            conn.commit()

    def get_flashcards(self, source_id: str) -> FlashcardSet:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT front, back, explanation FROM flashcards WHERE document_id = ?",
                (source_id,)
            )
            rows = cursor.fetchall()

        cards = [
            FlashcardItem(
                front=row["front"],
                back=row["back"],
                explanation=row["explanation"]
            )
            for row in rows
        ]
        return FlashcardSet(cards=cards)

flashcard_service = FlashcardService()
