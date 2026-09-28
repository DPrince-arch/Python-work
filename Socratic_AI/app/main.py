from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from api.documents import router as documents_router
from api.chats import router as chat_router
from api.flashcards import router as flashcards_router
from api.quiz import router as quiz_router
from app.database import init_db

init_db()

app = FastAPI(
    title="Socratic AI Study Suite",
    description="Unified Socratic Tutor, Notes-to-Flashcards RAG Engine, and Adaptive Mastery Quizzer grounded in uploaded notes.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents_router)
app.include_router(chat_router)
app.include_router(flashcards_router)
app.include_router(quiz_router)

static_dir = Path(__file__).resolve().parent.parent / "static"
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/", StaticFiles(directory=str(static_dir), html=True), name="static")
