from fastapi import APIRouter
from app.schema import GenerateFlashcardsRequest, FlashcardSet
from services.flash_service import flashcard_service

router = APIRouter(prefix="/api/flashcards", tags=["flashcards"])

@router.post("/generate", response_model=FlashcardSet)
async def generate_flashcards(payload: GenerateFlashcardsRequest):
    return flashcard_service.generate_flashcards(
        document_id=payload.document_id,
        topic_name=payload.topic_name,
        num_cards=payload.num_cards
    )

@router.get("/{source_id}", response_model=FlashcardSet)
async def get_flashcards(source_id: str):
    """Retrieve existing flashcards for a document or topic."""
    return flashcard_service.get_flashcards(source_id)
