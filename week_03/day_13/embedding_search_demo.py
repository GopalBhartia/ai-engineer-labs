from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass(frozen=True)
class Document:
    """A small document that can be searched using semantic similarity."""

    doc_id: int
    title: str
    text: str
    category: str


@dataclass(frozen=True)
class SearchResult:
    """One ranked search result returned by semantic search."""

    doc: Document
    score: float


DOCUMENTS: list[Document] = [
    Document(
        doc_id=1,
        title="Password reset",
        text=(
            "Users can reset their account password from the security settings page."
        ),
        category="account",
    ),
    Document(
        doc_id=2,
        title="Two-factor authentication",
        text="Enable two-factor authentication to make your login more secure.",
        category="account",
    ),
    Document(
        doc_id=3,
        title="Billing invoice",
        text="Monthly invoices are available in the billing dashboard.",
        category="billing",
    ),
    Document(
        doc_id=4,
        title="Cancel subscription",
        text="You can cancel your subscription from the plan management page.",
        category="billing",
    ),
    Document(
        doc_id=5,
        title="Refund policy",
        text="Refunds are processed within seven business days after approval.",
        category="billing",
    ),
    Document(
        doc_id=6,
        title="FastAPI basics",
        text=(
            "FastAPI is a Python framework for building APIs with automatic "
            "documentation."
        ),
        category="engineering",
    ),
    Document(
        doc_id=7,
        title="Docker containers",
        text=(
            "Docker packages an application with its dependencies into a "
            "portable container."
        ),
        category="engineering",
    ),
    Document(
        doc_id=8,
        title="CI pipeline",
        text="A CI pipeline automatically runs tests and checks when code is pushed.",
        category="engineering",
    ),
    Document(
        doc_id=9,
        title="Model evaluation",
        text=(
            "Accuracy, precision, recall, and F1 score are common machine "
            "learning metrics."
        ),
        category="machine-learning",
    ),
    Document(
        doc_id=10,
        title="Overfitting",
        text=(
            "Overfitting happens when a model memorizes training data and "
            "fails on new data."
        ),
        category="machine-learning",
    ),
    Document(
        doc_id=11,
        title="Embeddings",
        text="Embeddings convert text into vectors that capture semantic meaning.",
        category="rag",
    ),
    Document(
        doc_id=12,
        title="Vector search",
        text="Vector search retrieves documents by comparing embedding similarity.",
        category="rag",
    ),
    Document(
        doc_id=13,
        title="RAG overview",
        text=(
            "Retrieval augmented generation uses relevant documents to ground "
            "LLM answers."
        ),
        category="rag",
    ),
    Document(
        doc_id=14,
        title="Prompt templates",
        text="Prompt templates help standardize instructions sent to a language model.",
        category="llm",
    ),
    Document(
        doc_id=15,
        title="Structured outputs",
        text="Structured outputs make LLM responses easier to validate and parse.",
        category="llm",
    ),
    Document(
        doc_id=16,
        title="Context window",
        text="A context window limits how much text a language model can read at once.",
        category="llm",
    ),
    Document(
        doc_id=17,
        title="Deployment",
        text=(
            "Production deployment requires environment variables, logging, "
            "and monitoring."
        ),
        category="devops",
    ),
    Document(
        doc_id=18,
        title="Environment variables",
        text=(
            "Environment variables store configuration such as API keys "
            "outside the code."
        ),
        category="devops",
    ),
    Document(
        doc_id=19,
        title="PyTorch training",
        text=(
            "A PyTorch training loop usually includes a model, loss function, "
            "and optimizer."
        ),
        category="machine-learning",
    ),
    Document(
        doc_id=20,
        title="Tokenization",
        text=(
            "Tokenization splits text into smaller units that language models "
            "can process."
        ),
        category="llm",
    ),
]


def create_document_texts(documents: list[Document]) -> list[str]:
    """Combine title and text so both are included in the embedding."""

    return [f"{doc.title}. {doc.text}" for doc in documents]


def normalize_embeddings(embeddings: np.ndarray) -> np.ndarray:
    """Normalize embeddings so cosine similarity becomes a dot product."""

    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)

    # Avoid division by zero in rare cases.
    safe_norms = np.where(norms == 0, 1, norms)

    return embeddings / safe_norms


def search(
    query: str,
    model: SentenceTransformer,
    documents: list[Document],
    document_embeddings: np.ndarray,
    top_k: int = 3,
) -> list[SearchResult]:
    """Search documents using cosine similarity."""

    query_embedding = model.encode([query], convert_to_numpy=True)
    query_embedding = normalize_embeddings(query_embedding)

    similarities = np.dot(document_embeddings, query_embedding[0])

    ranked_indexes = np.argsort(similarities)[::-1][:top_k]

    return [
        SearchResult(
            doc=documents[index],
            score=float(similarities[index]),
        )
        for index in ranked_indexes
    ]


def print_results(query: str, results: list[SearchResult]) -> None:
    """Print search results in a readable format."""

    print("=" * 80)
    print(f"Query: {query}")
    print("-" * 80)

    for rank, result in enumerate(results, start=1):
        print(f"{rank}. {result.doc.title}")
        print(f"   Score   : {result.score:.4f}")
        print(f"   Category: {result.doc.category}")
        print(f"   Text    : {result.doc.text}")
        print()


def main() -> None:
    """Run a small semantic search demo."""

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)

    document_texts = create_document_texts(DOCUMENTS)

    raw_document_embeddings = model.encode(document_texts, convert_to_numpy=True)
    document_embeddings = normalize_embeddings(raw_document_embeddings)

    queries = [
        "How can I change my password?",
        "Where can I see my payment invoice?",
        "How do embeddings help search?",
        "What should I use to deploy my API?",
        "How do I evaluate a machine learning model?",
    ]

    for query in queries:
        results = search(
            query=query,
            model=model,
            documents=DOCUMENTS,
            document_embeddings=document_embeddings,
            top_k=3,
        )
        print_results(query=query, results=results)


if __name__ == "__main__":
    main()
