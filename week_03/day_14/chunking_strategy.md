# Day 14 - Chunking Strategy Notes

## What is chunking?

Chunking means splitting a large document into smaller text pieces before embedding and storing them in a vector database.

Example:

```text
Large PDF or Markdown file
    -> chunk 1
    -> chunk 2
    -> chunk 3
```

## Why chunking matters

Chunking matters because retrieval quality depends heavily on the quality of chunks.

If chunks are too large:

- They may contain too many unrelated ideas.
- Retrieval may return noisy context.
- The LLM may receive unnecessary information.
- Token cost may increase.

If chunks are too small:

- Important context may be missing.
- The answer may become incomplete.
- The LLM may not understand the full meaning.
- Related information may be split across too many chunks.

## Good chunking goal

A good chunk should contain one clear idea with enough surrounding context.

Example of a good chunk:

```text
FastAPI is a Python framework for building APIs.
It provides automatic validation using Pydantic models and automatic documentation using Swagger UI.
```

This chunk is useful because it has a complete idea.

Example of a bad chunk:

```text
automatic documentation using
```

This chunk is bad because it has no complete meaning.

## Chunk size

For this project, a good starting point is:

```text
300-500 words per chunk
```

This is not a strict rule. The best chunk size depends on the type of document.

For short notes:

```text
200-300 words may be enough
```

For detailed technical documents:

```text
400-800 words may work better
```

## Chunk overlap

Chunk overlap means repeating a small part of one chunk in the next chunk.

Example:

```text
Chunk 1: paragraphs 1, 2, 3
Chunk 2: paragraphs 3, 4, 5
```

Paragraph 3 is repeated.

Overlap helps preserve context across chunk boundaries.

For this project, a good starting point is:

```text
50-100 words overlap
```

## Types of chunking

### 1. Fixed-size chunking

Fixed-size chunking splits text every fixed number of words or tokens.

Example:

```text
Every 500 words = one chunk
```

Pros:

- Simple
- Easy to implement
- Fast

Cons:

- Can split ideas in the middle
- May break paragraphs or sections

### 2. Paragraph-based chunking

Paragraph-based chunking splits text based on paragraphs.

Pros:

- Preserves natural meaning
- Easy to understand
- Good for notes and Markdown files

Cons:

- Some paragraphs may be too short or too long

### 3. Heading-based chunking

Heading-based chunking splits text based on document headings.

Example:

```markdown
# Introduction

## Installation

## API Usage
```

Pros:

- Very useful for Markdown and documentation
- Keeps sections meaningful
- Preserves document structure

Cons:

- Depends on good document headings
- Poorly structured documents may not work well

### 4. Semantic chunking

Semantic chunking splits text based on meaning instead of only length.

Pros:

- High-quality chunks
- Better for complex documents
- Keeps related ideas together

Cons:

- More complex to implement
- May require extra models or libraries
- Can be slower

## Chosen strategy for this project

For the first version of this roadmap RAG project, use:

```text
Heading-aware + paragraph-aware chunking
```

The strategy:

```text
1. Read Markdown or PDF text.
2. Split by headings when available.
3. Split long sections into paragraph groups.
4. Keep each chunk around 300-500 words.
5. Add 50-100 words of overlap.
6. Store metadata with every chunk.
```

## Metadata to store with every chunk

Each chunk should store:

- source file
- chunk index
- page number if PDF
- section heading if available
- created date

Example metadata:

```json
{
  "source_file": "rag_notes.md",
  "chunk_index": 3,
  "page_number": null,
  "section_heading": "Chunking",
  "created_at": "2026-06-10"
}
```

## Why metadata matters

Metadata is important for:

- citations
- debugging retrieval
- filtering search results
- showing source documents
- evaluating answer quality

## Example chunk record

```json
{
  "id": "rag_notes_chunk_003",
  "text": "Chunking means splitting a large document into smaller text pieces before embedding and storing them in a vector database.",
  "metadata": {
    "source_file": "rag_notes.md",
    "chunk_index": 3,
    "section_heading": "Chunking"
  }
}
```

## Simple rule to remember

The goal is not to create perfect chunks.

The goal is to create chunks that are:

```text
small enough to search accurately
large enough to preserve meaning
traceable enough to cite
```

## Final Summary

Chunking is one of the most important parts of RAG.

Bad chunking leads to bad retrieval.

Bad retrieval leads to weak LLM answers.

Good chunking makes the system easier to search, easier to cite, and easier to trust.