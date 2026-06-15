# Day 17 - RAG Evaluation Basics

## Goal

Learn how to evaluate a Retrieval-Augmented Generation (RAG) system.

---

## Why Evaluation Matters

A RAG system can appear to work even when:

- Retrieval returns the wrong documents.
- Citations are missing.
- The model hallucinates.
- Refusal behavior fails.

Evaluation helps measure quality objectively.

---

## Golden Dataset

A golden dataset contains:

- Question
- Expected source document

Example:

| Question | Expected Source |
|-----------|-----------|
| What is FastAPI? | fastapi_notes.md |
| What is RAG? | rag_notes.md |

---

## Retrieval Hit Rate

Measures whether retrieval found the expected document.

Formula:

Hit Rate = Correct Retrievals / Total Questions

Result:

- Hits: 9/9
- Hit Rate: 100%

---

## Automated Tests

### Citation Test

Verify answers contain citations.

### Refusal Test

Verify the system refuses questions that cannot be answered using available documents.

Example:

Question:

Who won the FIFA World Cup in 1978?

Expected:

I cannot answer this question using the available documents.

---

## Common RAG Metrics

### Context Recall

Did retrieval find the necessary information?

### Context Precision

How much retrieved information was actually useful?

### Faithfulness

Did the answer remain grounded in the retrieved context?

### Answer Relevancy

Did the answer address the user's question?

---

## Evaluation Tools

### Ragas

Used for:

- Faithfulness
- Answer Relevancy
- Context Recall
- Context Precision

### TruLens

Used for:

- Groundedness
- Retrieval quality
- Evaluation dashboards

---

## Key Learning

A working RAG system is not enough.

A production-quality RAG system must also be measurable and testable.