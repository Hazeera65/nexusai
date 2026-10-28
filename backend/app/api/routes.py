
from fastapi import APIRouter
from app.schemas.document import (
    DocumentPreviewRequest,
    DocumentPreviewResponse,
)

router = APIRouter(prefix="/api/v1", tags=["NexusAI"])


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "nexusai-api",
        "version": "0.2.0",
    }


@router.post(
    "/documents/preview",
    response_model=DocumentPreviewResponse,
)
def preview_document(
    document: DocumentPreviewRequest,
) -> DocumentPreviewResponse:
    return DocumentPreviewResponse(
        title=document.title.strip(),
        character_count=len(document.content),
        status="validated",
    )
