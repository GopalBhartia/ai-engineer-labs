from __future__ import annotations

from pydantic import BaseModel


class Citation(BaseModel):
    source: str
    section: str


class RAGResponse(BaseModel):
    answer: str
    citations: list[Citation]
