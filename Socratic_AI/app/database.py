import sqlite3
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import settings

def get_db():
    try:
        conn = psycopg2.connect(settings.sync_database_url)
        return PostgreSQLWrapper(conn)
    except Exception:
        sqlite_conn = sqlite3.connect(settings.DATA_DIR / "socratic_suite.db")
        sqlite_conn.row_factory = sqlite3.Row
        return SQLiteWrapper(sqlite_conn)

class PostgreSQLWrapper:
    def __init__(self, conn):
        self.conn = conn

    def cursor(self):
        return PostgreSQLCursorWrapper(self.conn.cursor(cursor_factory=RealDictCursor))

    def commit(self):
        self.conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

class PostgreSQLCursorWrapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query: str, params: tuple = ()):
        pg_query = query.replace("?", "%s")
        if "INSERT OR REPLACE INTO" in pg_query:
            pg_query = pg_query.replace("INSERT OR REPLACE INTO", "INSERT INTO")
            if "quiz_questions" in pg_query:
                pg_query += " ON CONFLICT (id) DO UPDATE SET question_text = EXCLUDED.question_text, options_json = EXCLUDED.options_json, correct_answer = EXCLUDED.correct_answer, explanation = EXCLUDED.explanation, concept = EXCLUDED.concept, difficulty = EXCLUDED.difficulty"
            elif "mastery_scores" in pg_query:
                pg_query += " ON CONFLICT (document_id, concept) DO UPDATE SET score = EXCLUDED.score, attempts = EXCLUDED.attempts"

        self.cursor.execute(pg_query, params)
        return self

    def fetchone(self):
        res = self.cursor.fetchone()
        return dict(res) if res else None

    def fetchall(self):
        res = self.cursor.fetchall()
        return [dict(r) for r in res] if res else []

class SQLiteWrapper:
    def __init__(self, conn):
        self.conn = conn

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

def init_db():
    with get_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id VARCHAR(255) PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            file_type VARCHAR(50) NOT NULL,
            text_content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS document_chunks (
            id VARCHAR(255) PRIMARY KEY,
            document_id VARCHAR(255) NOT NULL,
            chunk_index INTEGER NOT NULL,
            text TEXT NOT NULL,
            embedding TEXT NOT NULL
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_sessions (
            id VARCHAR(255) PRIMARY KEY,
            document_id VARCHAR(255) NOT NULL,
            title VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
            id SERIAL PRIMARY KEY,
            session_id VARCHAR(255) NOT NULL,
            role VARCHAR(50) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id VARCHAR(255) PRIMARY KEY,
            document_id VARCHAR(255) NOT NULL,
            front TEXT NOT NULL,
            back TEXT NOT NULL,
            explanation TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id VARCHAR(255) PRIMARY KEY,
            document_id VARCHAR(255) NOT NULL,
            question_text TEXT NOT NULL,
            options_json TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            explanation TEXT NOT NULL,
            concept VARCHAR(255) NOT NULL,
            difficulty VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mastery_scores (
            id SERIAL PRIMARY KEY,
            document_id VARCHAR(255) NOT NULL,
            concept VARCHAR(255) NOT NULL,
            score REAL NOT NULL,
            attempts INTEGER DEFAULT 1,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_doc_concept UNIQUE (document_id, concept)
        );
        """)
        
        conn.commit()

init_db()