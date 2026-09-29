from typing import Optional
import uuid
from fastapi import APIRouter, Header
from fastapi.responses import StreamingResponse
from app.schema import ChatRequest
from services.socratic_service import socratic_service
from app.database import get_db

router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.post("/stream")
async def stream_chat(payload: ChatRequest, x_socratic_api_key: Optional[str] = Header(None, alias="X-Socratic-Api-Key")):
    session_id = payload.session_id or str(uuid.uuid4())
    doc_id = payload.document_id
    topic_name = payload.topic_name
    source_title = doc_id or topic_name or "General Study"
    
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM chat_sessions WHERE id = ?", (session_id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO chat_sessions (id, document_id, title) VALUES (?, ?, ?)", (session_id, source_title, f"Session - {payload.message[:30]}"))
        
        cursor.execute("INSERT INTO chat_messages (session_id, role, content) VALUES (?, ?, ?)", (session_id, "user", payload.message))
        
        cursor.execute("SELECT role, content FROM chat_messages WHERE session_id = ? ORDER BY id ASC", (session_id,))
        rows = cursor.fetchall()
        history = [{"role": row["role"], "content": row["content"]} for row in rows[:-1]]
        conn.commit()

    async def socratic_stream_wrapper():
        full_reply = []
        yield f"data: [SESSION_ID:{session_id}]\n\n"
        
        async for chunk in socratic_service.stream_socratic_response(
            doc_id, topic_name, payload.message, history,
            api_key=x_socratic_api_key
            ):
            if chunk.startswith("data: ") and not chunk.endswith("[DONE]\n\n") and not chunk.startswith("data: [SESSION_ID:"):
                text_piece = chunk.replace("data: ", "").replace("\n\n", "")
                full_reply.append(text_piece)
            yield chunk

        ai_message = "".join(full_reply).strip()
        if ai_message:
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO chat_messages (session_id, role, content) VALUES (?, ?, ?)", (session_id, "model", ai_message))
                conn.commit()

    return StreamingResponse(socratic_stream_wrapper(), media_type="text/event-stream")