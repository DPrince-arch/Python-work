import uuid
import json
import math
import io
from typing import List
from app.config import settings
from app.database import get_db

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

class RAGService:
    def extract_text(self, filename: str, content_bytes: bytes) -> str:
        if filename.endswith(".pdf"):
            if PdfReader is None:
                raise ValueError("pypdf is required to parse PDF files.")
            reader = PdfReader(io.BytesIO(content_bytes))
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text.strip()
        else:
            return content_bytes.decode("utf-8", errors="ignore").strip()

    def chunk_text(self, text: str, chunk_size: int = None, overlap: int = None) -> List[str]:
        chunk_size = chunk_size or settings.DEFAULT_CHUNK_SIZE
        overlap = overlap or settings.DEFAULT_CHUNK_OVERLAP
        
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""

        for para in paragraphs:
            para = para.strip()
            if not para: continue
            if len(current_chunk) + len(para) <= chunk_size:
                current_chunk += ("\n\n" if current_chunk else "") + para
            else:
                if current_chunk: chunks.append(current_chunk)
                current_chunk = para

        if current_chunk: chunks.append(current_chunk)
        return chunks if chunks else [text]

    def _generate_embedding(self, text: str) -> List[float]:
        if settings.GEMINI_API_KEY:
            try:
                from google import genai
                client = genai.Client(api_key=settings.GEMINI_API_KEY)
                response = client.models.embed_content(
                    model=settings.EMBEDDING_MODEL,
                    contents=text
                )
                return response.embedding.values
            except Exception as e:
                print(f"[RAGService] Gemini Embedding API error: {e}")

        words = [w.lower() for w in text.split() if len(w) > 2]
        vocab = sorted(list(set(words)))[:100]
        vec = [float(words.count(w)) for w in vocab]
        norm = math.sqrt(sum(v*v for v in vec)) or 1.0
        return [v / norm for v in vec]

    def process_and_store_document(self, filename: str, content_bytes: bytes) -> str:
        doc_id = str(uuid.uuid4())
        file_type = "pdf" if filename.endswith(".pdf") else "text"
        raw_text = self.extract_text(filename, content_bytes)

        if not raw_text:
            raise ValueError("Document appears to be empty or unreadable.")

        chunks = self.chunk_text(raw_text)

        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO documents (id, filename, file_type, text_content) VALUES (?, ?, ?, ?)",
                (doc_id, filename, file_type, raw_text)
            )

            for idx, chunk_str in enumerate(chunks):
                chunk_id = f"{doc_id}-{idx}"
                embedding_vec = self._generate_embedding(chunk_str)
                cursor.execute(
                    "INSERT INTO document_chunks (id, document_id, chunk_index, text, embedding) VALUES (?, ?, ?, ?, ?)",
                    (chunk_id, doc_id, idx, chunk_str, json.dumps(embedding_vec))
                )
            conn.commit()

        return doc_id

    def get_relevant_chunks(self, document_id: str, query: str, top_k: int = 4) -> List[str]:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT text, embedding FROM document_chunks WHERE document_id = ?", (document_id,))
            rows = cursor.fetchall()

        if not rows: return []
        if not query.strip(): return [row["text"] for row in rows[:top_k]]

        query_vec = self._generate_embedding(query)

        def cosine_similarity(v1: List[float], v2: List[float]) -> float:
            min_len = min(len(v1), len(v2))
            if min_len == 0: return 0.0
            dot = sum(v1[i] * v2[i] for i in range(min_len))
            norm1 = math.sqrt(sum(v1[i]**2 for i in range(min_len))) or 1.0
            norm2 = math.sqrt(sum(v2[i]**2 for i in range(min_len))) or 1.0
            return dot / (norm1 * norm2)

        scored_chunks = []
        for row in rows:
            chunk_text = row["text"]
            chunk_vec = json.loads(row["embedding"])
            score = cosine_similarity(query_vec, chunk_vec)
            scored_chunks.append((score, chunk_text))

        scored_chunks.sort(key=lambda x: x[0], reverse=True)
        return [c[1] for c in scored_chunks[:top_k]]

rag_service = RAGService()