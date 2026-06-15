from __future__ import annotations


def build_rag_prompt(question: str, context: str) -> str:
    return f"""
You are a helpful question-answering assistant.

Use ONLY the provided context to answer.

If the answer cannot be found in the context,
respond exactly with:

I cannot answer this question using the available documents.

Context:
---------
{context}

Question:
{question}
""".strip()
