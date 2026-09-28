from pydantic import BaseModel, Field
from typing import List, Optional

class DocumentInfo(BaseModel):
    id: str
    filename: str
    file_type: str
    created_at: str

class DocumentUploadResponse(BaseModel):
    document_id: str
    filename: str
    chunks_count: int
    message: str

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    document_id: Optional[str] = None
    topic_name: Optional[str] = None
    message: str

class ChatSessionInfo(BaseModel):
    session_id: str
    document_id: Optional[str] = None
    topic_name: Optional[str] = None
    created_at: str
    messages: List[ChatMessage]

class FlashcardItem(BaseModel):
    front: str = Field(description="Front of card: Key question or prompt")
    back: str = Field(description="Back of card: Clear answer")
    explanation: str = Field(description="Contextual explanation")

class FlashcardSet(BaseModel):
    cards: List[FlashcardItem]

class GenerateFlashcardsRequest(BaseModel):
    document_id: Optional[str] = None
    topic_name: Optional[str] = None
    num_cards: int = Field(default=5, ge=1, le=20)

class QuizQuestion(BaseModel):
    id: str = Field(description="Unique question identifier")
    question_text: str = Field(description="Question text derived from notes or topic")
    options: List[str] = Field(description="10 multiple choice options")
    correct_answer: str = Field(description="Exact string of the correct option")
    explanation: str = Field(description="Explanation grounded in theory")
    concept: str = Field(description="Concept/topic being tested")
    difficulty: str = Field(description="'Beginner', 'Intermediate', or 'Advanced'")

class QuizSet(BaseModel):
    topic: str
    questions: List[QuizQuestion]

class GenerateQuizRequest(BaseModel):
    document_id: Optional[str] = None
    topic_name: Optional[str] = None
    num_questions: int = Field(default=10, ge=1, le=20)

class QuizSubmissionItem(BaseModel):
    question_id: str
    selected_option: str

class QuizSubmitRequest(BaseModel):
    document_id: Optional[str] = None
    topic_name: Optional[str] = None
    answers: List[QuizSubmissionItem]

class QuizResultItem(BaseModel):
    question_id: str
    question_text: str
    user_answer: str
    correct_answer: str
    is_correct: bool
    explanation: str
    concept: str

class QuizFeedback(BaseModel):
    total_questions: int
    score: int
    percentage: float
    results: List[QuizResultItem]
    suggested_topics: List[str] = Field(default_factory=list, description="Topics recommended for study based on missed questions")

class MasteryMetric(BaseModel):
    concept: str
    score: float
    attempts: int

class MasterySummary(BaseModel):
    source_identifier: str
    mastery_metrics: List[MasteryMetric]