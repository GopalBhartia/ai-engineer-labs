from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from week_03.day_16.rag_service import answer_question
from week_03.day_16.schemas import RAGResponse

app = FastAPI()


class QueryRequest(BaseModel):
    question: str


@app.post(
    "/rag/query",
    response_model=RAGResponse,
)
def rag_query(
    request: QueryRequest,
) -> RAGResponse:
    return answer_question(request.question)
