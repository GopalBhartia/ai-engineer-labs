from __future__ import annotations

from week_03.day_16.rag_service import answer_question


def test_answer_contains_citations() -> None:
    response = answer_question("What is FastAPI?")

    assert len(response.citations) > 0


def test_refusal_behavior() -> None:
    response = answer_question("Who won the FIFA World Cup in 1978?")

    assert "cannot answer" in response.answer.lower()
