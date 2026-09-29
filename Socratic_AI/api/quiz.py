from typing import Optional
from fastapi import APIRouter, Header
from app.schema import (
    GenerateQuizRequest, QuizSet, 
    QuizSubmitRequest, QuizFeedback, MasterySummary
)
from services.quiz_service import quiz_service

router = APIRouter(prefix="/api/quiz", tags=["quiz"])

@router.post("/generate", response_model=QuizSet)
async def generate_quiz(payload: GenerateQuizRequest, x_quiz_api_key: Optional[str] = Header(None, alias="X-Quiz-Api-Key")):
    return quiz_service.generate_quiz(
        document_id=payload.document_id,
        topic_name=payload.topic_name,
        num_questions=payload.num_questions,
        api_key=x_quiz_api_key,
    )

@router.post("/submit", response_model=QuizFeedback)
async def submit_quiz(payload: QuizSubmitRequest):
    return quiz_service.submit_quiz(payload)

@router.get("/mastery/{source_id}", response_model=MasterySummary)
async def get_mastery(source_id: str):
    return quiz_service.get_mastery_summary(source_id)
