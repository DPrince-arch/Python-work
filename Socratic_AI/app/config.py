import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "cerebras")
    CEREBRAS_MODEL_NAME: str = os.getenv("CEREBRAS_MODEL_NAME", "llama-3.3-70b")
    CEREBRAS_API_KEY: str = os.getenv("CEREBRAS_API_KEY", "")
    SOCRATIC_CEREBRAS_API_KEY: Optional[str] = os.getenv("SOCRATIC_CEREBRAS_API_KEY")
    FLASHCARD_CEREBRAS_API_KEY: Optional[str] = os.getenv("FLASHCARD_CEREBRAS_API_KEY")
    QUIZ_CEREBRAS_API_KEY: Optional[str] = os.getenv("QUIZ_CEREBRAS_API_KEY")

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    SOCRATIC_GEMINI_API_KEY: Optional[str] = os.getenv("SOCRATIC_GEMINI_API_KEY")
    FLASHCARD_GEMINI_API_KEY: Optional[str] = os.getenv("FLASHCARD_GEMINI_API_KEY")
    QUIZ_GEMINI_API_KEY: Optional[str] = os.getenv("QUIZ_GEMINI_API_KEY")
    EMBEDDING_GEMINI_API_KEY: Optional[str] = os.getenv("EMBEDDING_GEMINI_API_KEY")

    MODEL_NAME: str = "gemini-2.5-flash"
    EMBEDDING_MODEL: str = "text-embedding-004"
    
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "socratic_suite")
    
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")

    @property
    def sync_database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    DATA_DIR: Path = BASE_DIR / "data"
    MAX_HISTORY_MESSAGES: int = 12
    DEFAULT_CHUNK_SIZE: int = 600
    DEFAULT_CHUNK_OVERLAP: int = 100

    def get_cerebras_key(self, mode: str, header_key: Optional[str] = None) -> str:
        if header_key and header_key.strip():
            return header_key.strip()
        
        mode_keys = {
            "socratic": self.SOCRATIC_CEREBRAS_API_KEY,
            "flashcard": self.FLASHCARD_CEREBRAS_API_KEY,
            "quiz": self.QUIZ_CEREBRAS_API_KEY,
        }
        val = mode_keys.get(mode.lower())
        if val and val.strip():
            return val.strip()

        return self.CEREBRAS_API_KEY

    def get_api_key(self, mode: str, header_key: Optional[str] = None) -> str:
        if header_key and header_key.strip():
            return header_key.strip()
        
        mode_keys = {
            "socratic": self.SOCRATIC_GEMINI_API_KEY,
            "flashcard": self.FLASHCARD_GEMINI_API_KEY,
            "quiz": self.QUIZ_GEMINI_API_KEY,
            "embedding": self.EMBEDDING_GEMINI_API_KEY,
        }
        val = mode_keys.get(mode.lower())
        if val and val.strip():
            return val.strip()

        return self.GEMINI_API_KEY

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
settings.DATA_DIR.mkdir(parents=True, exist_ok=True)
