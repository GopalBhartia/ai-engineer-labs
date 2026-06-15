from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

from week_03.day_15.vector_db_demo import search_documents
from week_03.day_16.prompt_builder import build_rag_prompt
from week_03.day_16.schemas import Citation, RAGResponse

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_context(results: list) -> str:
    """
    Convert retrieved Qdrant chunks into a formatted context block.
    """

    context_parts = []

    for idx, point in enumerate(results, start=1):
        text = point.payload.get("text", "")

        context_parts.append(f"[{idx}]\n{text}")

    return "\n\n".join(context_parts)


def build_citations(results: list) -> list[Citation]:
    """
    Extract citation metadata from retrieved chunks.
    """

    citations = []

    for point in results:
        payload = point.payload

        citations.append(
            Citation(
                source=payload.get("source", "unknown"),
                section=payload.get("section", "unknown"),
            )
        )

    return citations


def answer_question(question: str) -> RAGResponse:
    """
    Complete RAG pipeline:
    1. Retrieve relevant chunks from Qdrant
    2. Build context
    3. Generate prompt
    4. Call OpenAI
    5. Return answer + citations
    """
    results = search_documents(question)

    if not results:
        return RAGResponse(
            answer=("I cannot answer this question using the available documents."),
            citations=[],
        )

    best_score = results[0].score

    if best_score < 0.5:
        return RAGResponse(
            answer=("I cannot answer this question using the available documents."),
            citations=[],
        )

    context = build_context(results)

    prompt = build_rag_prompt(
        question=question,
        context=context,
    )

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    answer = response.output_text

    return RAGResponse(
        answer=answer,
        citations=build_citations(results),
    )
