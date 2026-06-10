# Day 14 - RAG Architecture

## What is RAG?

RAG means **Retrieval-Augmented Generation**.

A normal LLM answers from its trained knowledge and from the prompt. A RAG system first retrieves relevant information from external documents, then gives that information to the LLM as context.

Simple flow:

```text
User question -> Retrieve relevant documents -> Give context to LLM -> Generate answer with citations
```

RAG is useful because it helps the model answer using private, updated, or domain-specific data without retraining the model.

## Why RAG is useful

RAG helps with:

- Reducing hallucinations
- Answering from private documents
- Adding source citations
- Updating knowledge without fine-tuning
- Building document question-answering systems
- Making LLM apps more grounded and trustworthy

## Main RAG Components

### 1. Ingestion

Ingestion means collecting documents into the system.

Examples:

- PDFs
- Markdown files
- Text files
- CSV files
- Web pages
- Internal company documents

In this project, sample documents are stored in:

```text
week_03/day_14/data/sample_docs/
```

### 2. Parsing

Parsing means extracting clean text from documents.

Examples:

```text
PDF -> text
Markdown -> text
HTML -> clean article text
CSV -> row-based text
```

Good parsing is important because bad extracted text creates bad chunks, bad chunks create bad retrieval, and bad retrieval creates weak answers.

### 3. Chunking

Chunking means splitting long documents into smaller pieces.

Example:

```text
Large document -> chunk 1, chunk 2, chunk 3
```

Chunking is needed because:

- Large documents may not fit into an LLM context window.
- Smaller chunks are easier to search.
- Retrieval works better when each chunk contains one clear idea.
- The LLM should receive only the most relevant context.

### 4. Embedding

An embedding is a numerical representation of text.

Example text:

```text
FastAPI is used to build APIs.
```

The embedding model converts it into a vector like:

```text
[0.12, -0.44, 0.88, ...]
```

The vector captures semantic meaning. Similar text should have similar vectors.

For example, these two sentences are semantically related:

```text
How do I create an API in Python?
```

```text
FastAPI is a Python framework for building APIs.
```

Even though the exact words are different, their meanings are close.

### 5. Vector Database

A vector database stores embeddings and allows similarity search.

A stored chunk usually contains:

- chunk id
- chunk text
- embedding vector
- metadata

Example metadata:

```json
{
  "source": "fastapi_notes.md",
  "chunk_index": 1,
  "page": null
}
```

Popular vector databases include:

- Pinecone
- Chroma
- FAISS
- Qdrant
- Weaviate
- Milvus

### 6. Retriever

The retriever finds the most relevant chunks for a user question.

Flow:

```text
User question -> query embedding -> vector search -> top matching chunks
```

The retriever is very important because the LLM can only answer well if it receives the right context.

If the retriever finds the wrong chunks, the LLM may give an incomplete or incorrect answer.

### 7. Generator

The generator is the LLM.

It receives:

- user question
- retrieved chunks
- instructions

Then it generates the final answer.

Example instruction:

```text
Answer using only the provided context.
If the answer is not present, say you do not know.
Include citations.
```

### 8. Citations

Citations show where the answer came from.

Example:

```text
Source: rag_notes.md, chunk 2
```

Citations usually come from metadata stored with each chunk.

Without metadata, it becomes difficult to tell the user where the answer came from.

## RAG Architecture Sketch

```text
Source documents
    |
    v
Ingestion
    |
    v
Parsing
    |
    v
Chunking
    |
    v
Embedding
    |
    v
Vector database
    |
    v
Retriever <--- User question
    |
    v
Relevant chunks
    |
    v
Generator / LLM
    |
    v
Answer with citations
```

## Example RAG Flow

User asks:

```text
What is chunk overlap?
```

System flow:

```text
1. Convert the question into an embedding.
2. Search the vector database.
3. Retrieve the most relevant chunks.
4. Send those chunks to the LLM.
5. Ask the LLM to answer using only the retrieved context.
6. Return the answer with citations.
```

Example answer:

```text
Chunk overlap means repeating a small part of one chunk in the next chunk so that important context is not lost.

Source: chunking_strategy.md, chunk 3
```

## Design Decision for This Project

For the first RAG version, the project will use:

```text
Document types: Markdown first, PDFs later
Chunking: heading-aware and paragraph-aware chunking
Chunk size: around 300-500 words
Overlap: around 50-100 words
Metadata: source file, chunk index, page number if available
Vector DB: local option first, hosted option later
Generator: hosted LLM API
Citations: source file + chunk id
```

## Final Summary

RAG is a way to make LLM apps answer from external knowledge.

The main idea is:

```text
Retrieve first, generate second.
```

This makes the answer more grounded, more useful, and easier to verify.

## Done Condition

Day 14 is complete when:

- RAG components are understood.
- Architecture notes are written.
- Sample data folder is created.
- Chunking strategy notes are written.
- Changes are committed to Git.