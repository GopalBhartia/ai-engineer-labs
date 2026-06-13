# Day 15 - Vector Database Setup

## Goal

The goal of Day 15 is to create a working vector database retrieval demo.

The system should:

```text
Read documents -> create chunks -> embed chunks -> store in Qdrant -> retrieve top-k relevant chunks
```

## Vector Database Chosen

For this project, I chose:

```text
Qdrant locally
```

Reason:

- It is open source.
- It works locally.
- It has a Python client.
- It supports metadata payloads.
- It is suitable for RAG projects.
- It can later be moved to Docker or cloud.

Optional future upgrade:

```text
Pinecone cloud
```

## What is a vector database?

A vector database stores embeddings.

An embedding is a numerical representation of text.

Example text:

```text
FastAPI is used to build APIs.
```

Example vector:

```text
[0.12, -0.44, 0.88, ...]
```

The vector captures meaning.

A vector database can search for similar meaning instead of only exact words.

## Why vector databases are useful in RAG

In RAG, the model should answer using relevant documents.

A vector database helps find those relevant documents.

Simple RAG retrieval flow:

```text
User question -> query embedding -> vector search -> top matching chunks
```

The matching chunks are later sent to the LLM as context.

## Qdrant concepts

### Collection

A collection is like a table in a database.

It stores many vectors.

Example collection name:

```text
ai_engineer_docs
```

### Point

A point is one stored item in Qdrant.

A point contains:

```text
id
vector
payload
```

### Payload

Payload means metadata attached to a vector.

For this project, every chunk stores:

```text
source
page
section
chunk_id
text
```

This metadata is important for citations and debugging.

## Metadata used

Each chunk stores:

```text
source: original file name
page: page number if available, otherwise null
section: section or heading name
chunk_id: unique id for the chunk
text: original chunk text
```

Example:

```json
{
  "source": "rag_notes.md",
  "page": null,
  "section": "RAG Notes",
  "chunk_id": "rag_notes.md_chunk_001",
  "text": "RAG means Retrieval-Augmented Generation..."
}
```

## Top-k retrieval

Top-k retrieval means returning the best k matching chunks.

Example:

```text
top_k = 3
```

This means the system returns the top 3 most relevant chunks for a question.

## Day 15 implementation flow

The Python demo does this:

```text
1. Load markdown files from Day 14 sample_docs.
2. Split each document into paragraph-aware chunks.
3. Load a sentence-transformers embedding model.
4. Convert every chunk into an embedding.
5. Create a Qdrant collection.
6. Upsert chunks into Qdrant with metadata.
7. Ask 10 test questions.
8. Print top-k results with score, source, page, section, chunk_id, and text.
```

## Files created

```text
week_03/day_15/vector_db_demo.py
week_03/day_15/vector_db_notes.md
```

The demo uses sample documents from:

```text
week_03/day_14/data/sample_docs/
```

## Test questions used

```text
1. What is RAG?
2. Why is RAG useful?
3. What are the components of a RAG system?
4. What is FastAPI used for?
5. How does FastAPI validate data?
6. What is Swagger UI?
7. What does an AI engineer do?
8. Why should AI apps be testable?
9. What is retrieval augmented generation?
10. Which documents talk about APIs?
```

## Expected result

For each question, the system should return the most relevant chunks.

Example:

```text
Question:
What is RAG?

Expected top source:
rag_notes.md
```

Example:

```text
Question:
What is FastAPI used for?

Expected top source:
fastapi_notes.md
```

## Important learning

Vector DB retrieval is not the same as keyword search.

Keyword search looks for exact words.

Vector search looks for meaning.

Example:

```text
Question:
How do I build an API in Python?

Relevant text:
FastAPI is a Python framework for building APIs.
```

These are related by meaning, even if the words are not exactly the same.

## Final summary

Day 15 connects RAG architecture to a working retrieval system.

The important flow is:

```text
Documents -> Chunks -> Embeddings -> Qdrant -> Top-k retrieval
```

The LLM is not added yet.

This day focuses only on the retrieval part of RAG.