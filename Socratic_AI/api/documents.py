from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from app.schema import DocumentUploadResponse, DocumentInfo
from services.rag_service import rag_service
from app.database import get_db

router = APIRouter(prefix="/api/documents", tags=["documents"])

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """Upload a TXT, MD, or PDF file to chunk, embed, and store in vector DB."""
    if not (file.filename.endswith(".txt") or file.filename.endswith(".md") or file.filename.endswith(".pdf")):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Please upload a .txt, .md, or .pdf file."
        )

    try:
        content_bytes = await file.read()
        doc_id = rag_service.process_and_store_document(file.filename, content_bytes)

        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) as count FROM document_chunks WHERE document_id = ?", (doc_id,))
            chunks_count = cursor.fetchone()["count"]

        return DocumentUploadResponse(
            document_id=doc_id,
            filename=file.filename,
            chunks_count=chunks_count,
            message="Document successfully processed and indexed!"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process document: {str(e)}")

@router.get("", response_model=List[DocumentInfo])
async def list_documents():
    """List all uploaded documents."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, filename, file_type, created_at FROM documents ORDER BY created_at DESC")
        rows = cursor.fetchall()
        
    return [
        DocumentInfo(
            id=row["id"],
            filename=row["filename"],
            file_type=row["file_type"],
            created_at=str(row["created_at"])
        )
        for row in rows
    ]
