# Day 13 - Embeddings and Similarity Search

## Goal

The goal of this lab is to understand how semantic search works using dense embeddings.

In this lab, we:

- Created 20 small sample documents.
- Used a Sentence Transformers model to convert documents into embeddings.
- Converted user queries into embeddings.
- Compared query embeddings with document embeddings using cosine similarity.
- Retrieved the top-k most similar documents.
- Studied where retrieval can make mistakes.

---

## Key Concepts

### Dense Embeddings

A dense embedding is a list of numbers that represents the meaning of text.

Example:

```text
"How do I reset my password?"
```

can be converted into a vector like:

```text
[0.12, -0.44, 0.89, ...]
```

The exact numbers are not manually interpreted by humans. The important idea is that texts with similar meanings should have similar vectors.

For example, these two texts should be close in embedding space:

```text
"How do I reset my password?"
"I forgot my password and need to change it."
```

Even though they do not use exactly the same words, their meaning is similar.

---

### Semantic Search

Semantic search means searching by meaning instead of exact keywords.

Traditional keyword search looks for matching words.

Semantic search looks for matching meaning.

Example query:

```text
"How do I change my password?"
```

A semantic search system can retrieve a document like:

```text
"Users can reset their account password from the security settings page."
```

because "change password" and "reset password" are semantically related.

---

### Cosine Similarity

Cosine similarity is a common way to compare two embedding vectors.

It measures how similar the direction of two vectors is.

Simple intuition:

```text
Same direction      -> very similar
Different direction -> less similar
```

In this lab, we normalized the embeddings first. After normalization, cosine similarity can be calculated using a dot product.

The important search line was:

```python
similarities = np.dot(document_embeddings, query_embedding[0])
```

This compares the query embedding with every document embedding and returns one score per document.

Higher score means the document is more similar to the query.

---

### Top-k Retrieval

Top-k retrieval means returning the best `k` results.

For example:

```python
top_k = 3
```

means the search system returns the 3 most similar documents.

This is useful because in RAG systems, we usually do not send all documents to the LLM. We only send the most relevant chunks.

---

### Rerankers

A reranker is a second-stage model that improves search results.

Basic retrieval flow:

```text
Query -> embedding search -> top 10 documents
```

Reranking flow:

```text
Query -> embedding search -> top 10 documents -> reranker -> better top 3 documents
```

Embedding search is fast and useful, but it can sometimes retrieve documents that are broadly related instead of exactly correct.

A reranker looks more carefully at the relationship between the query and each retrieved document.

In this lab, we did not implement a reranker yet. We only studied the concept.

---

## What the Code Does

The file used for this lab is:

```text
week_03/day_13/embedding_search_demo.py
```

The code follows this flow:

```text
1. Define 20 sample documents.
2. Load the Sentence Transformers model.
3. Convert each document into text using title + body.
4. Create embeddings for all documents.
5. Normalize the document embeddings.
6. Create embeddings for user queries.
7. Normalize the query embedding.
8. Compare query embedding with all document embeddings.
9. Sort documents by similarity score.
10. Print the top-k search results.
```

---

## Sample Queries Used

The script tested these queries:

```text
How can I change my password?
Where can I see my payment invoice?
How do embeddings help search?
What should I use to deploy my API?
How do I evaluate a machine learning model?
```

Each query was searched against the 20 local sample documents.

---

## Expected Good Matches

| Query | Expected Best Match | Why |
|---|---|---|
| How can I change my password? | Password reset | The query asks about changing/resetting a password. |
| Where can I see my payment invoice? | Billing invoice | The query asks about invoices and payments. |
| How do embeddings help search? | Embeddings / Vector search | The query asks about embeddings and search. |
| What should I use to deploy my API? | Deployment / Docker containers | The query asks about API deployment. |
| How do I evaluate a machine learning model? | Model evaluation | The query asks about ML metrics and evaluation. |

---

## Top-k Retrieval Mistakes and Observations

Embedding search usually finds relevant results, but it can still make mistakes.

A result can be wrong for different reasons:

- The document is broadly related but not the exact answer.
- The query is vague.
- Multiple documents have overlapping meaning.
- The document text is too short.
- The embedding model does not understand the project context deeply.
- The search system retrieves similar topics but does not reason like an LLM.

### Mistake Analysis Table

| Query | Possible Correct Result | Possible Wrong/Weak Top-k Result | Why This Can Happen |
|---|---|---|---|
| How can I change my password? | Password reset | Two-factor authentication | Both are about account security, but 2FA does not answer password reset directly. |
| Where can I see my payment invoice? | Billing invoice | Cancel subscription | Both are billing-related, but cancellation is not about invoices. |
| How do embeddings help search? | Embeddings / Vector search | RAG overview | RAG is related to retrieval, but the direct answer should focus on embeddings or vector search. |
| What should I use to deploy my API? | Deployment / Docker containers | CI pipeline | CI is related to software delivery, but it is not the same as deployment. |
| How do I evaluate a machine learning model? | Model evaluation | Overfitting | Overfitting is related to ML quality, but evaluation metrics are the direct answer. |

---

## Why Retrieval Mistakes Matter in RAG

In a RAG app, retrieval mistakes can lead to poor answers.

The RAG flow is:

```text
User question
   ↓
Retrieve relevant chunks
   ↓
Send chunks to LLM
   ↓
LLM generates answer using those chunks
```

If retrieval gives weak or wrong chunks, the LLM may produce an answer that is:

- incomplete,
- poorly grounded,
- missing citations,
- or based on irrelevant context.

This is why retrieval quality is extremely important.

---

## How to Improve Retrieval Later

Possible improvements:

1. Use better chunks

   Instead of very short documents, use well-sized chunks with enough context.

2. Add metadata filtering

   Example:

   ```text
   Only search billing documents for billing-related queries.
   ```

3. Increase top-k

   Instead of retrieving only 3 chunks, retrieve 10 and rerank them.

4. Use a reranker

   A reranker can reorder the top results and improve final relevance.

5. Improve query rewriting

   The user query can be rewritten into a clearer search query before retrieval.

6. Evaluate retrieval quality

   Track whether the expected document appears in the top 1, top 3, or top 5 results.

---

## Important Takeaways

- Embeddings convert text into numeric vectors.
- Semantic search compares meaning, not exact words.
- Cosine similarity is commonly used to compare embeddings.
- Normalized vectors allow cosine similarity to be calculated using a dot product.
- Top-k retrieval returns the most similar documents.
- Retrieval can still make mistakes, especially when topics overlap.
- RAG systems depend heavily on retrieval quality.
- Better chunking, metadata, reranking, and evaluation improve RAG performance.

---

## Day 13 Completion Summary

Completed:

- Learned dense embeddings.
- Learned cosine similarity.
- Learned semantic search.
- Learned what rerankers are.
- Used Sentence Transformers to embed 20 sample documents.
- Built local similarity search using NumPy.
- Documented top-k retrieval mistakes and observations.

Done condition:

```text
Embedding search demo.
```