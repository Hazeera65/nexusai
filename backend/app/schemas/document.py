
from pydantic import BaseModel, Field


class DocumentPreviewRequest(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    content: str = Field(min_length=1, max_length=5000)


class DocumentPreviewResponse(BaseModel):
    title: str
    character_count: int
    status: str
