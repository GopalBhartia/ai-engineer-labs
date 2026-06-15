from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from uuid import NAMESPACE_URL, uuid5

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "ai_engineer_docs"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_SIZE = 384
QDRANT_PATH = "./qdrant_data"

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

qdrant_client = QdrantClient(path=QDRANT_PATH)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "week_03" / "day_14" / "data" / "sample_docs"


def load_markdown_files(data_dir: Path) -> list[Path]:
    """Return all markdown files from the sample docs folder."""
    return sorted(data_dir.glob("*.md"))


def extract_section_title(text: str, default: str) -> str:
    """Extract the first markdown heading from a document."""
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()

    return default


def split_into_paragraph_chunks(
    text: str,
    source_name: str,
    max_words: int = 120,
) -> list[dict[str, Any]]:
    """
    Split markdown text into simple paragraph-aware chunks.

    This is intentionally simple for Day 15:
    - split by blank lines
    - group paragraphs until max_words is reached
    - preserve source, section, page, and chunk_id metadata
    """
    section = extract_section_title(text, default=source_name)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

    chunks: list[dict[str, Any]] = []
    current_parts: list[str] = []
    current_word_count = 0

    for paragraph in paragraphs:
        paragraph_word_count = len(paragraph.split())

        if current_parts and current_word_count + paragraph_word_count > max_words:
            chunk_index = len(chunks) + 1
            chunks.append(
                {
                    "text": "\n\n".join(current_parts),
                    "metadata": {
                        "source": source_name,
                        "page": None,
                        "section": section,
                        "chunk_id": f"{source_name}_chunk_{chunk_index:03d}",
                    },
                }
            )
            current_parts = []
            current_word_count = 0

        current_parts.append(paragraph)
        current_word_count += paragraph_word_count

    if current_parts:
        chunk_index = len(chunks) + 1
        chunks.append(
            {
                "text": "\n\n".join(current_parts),
                "metadata": {
                    "source": source_name,
                    "page": None,
                    "section": section,
                    "chunk_id": f"{source_name}_chunk_{chunk_index:03d}",
                },
            }
        )

    return chunks


def build_chunks(data_dir: Path) -> list[dict[str, Any]]:
    """Load markdown documents and convert them into chunks."""
    chunks: list[dict[str, Any]] = []

    markdown_files = load_markdown_files(data_dir)

    if not markdown_files:
        raise FileNotFoundError(f"No markdown files found in: {data_dir}")

    for file_path in markdown_files:
        text = file_path.read_text(encoding="utf-8")
        chunks.extend(
            split_into_paragraph_chunks(
                text=text,
                source_name=file_path.name,
            )
        )

    return chunks


def create_qdrant_collection(client: QdrantClient) -> None:
    """Create or recreate the Qdrant collection."""
    if client.collection_exists(collection_name=COLLECTION_NAME):
        client.delete_collection(collection_name=COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE,
        ),
    )


def stable_point_id(chunk_id: str) -> str:
    """Create a stable UUID from a chunk id."""
    return str(uuid5(NAMESPACE_URL, chunk_id))


def upsert_chunks(
    client: QdrantClient,
    model: SentenceTransformer,
    chunks: list[dict[str, Any]],
) -> None:
    """Embed chunks and upsert them into Qdrant."""
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts, normalize_embeddings=True)

    points = []

    for chunk, embedding in zip(chunks, embeddings, strict=True):
        metadata = chunk["metadata"]

        payload = {
            **metadata,
            "text": chunk["text"],
        }

        points.append(
            PointStruct(
                id=stable_point_id(metadata["chunk_id"]),
                vector=embedding.tolist(),
                payload=payload,
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )


def search_chunks(
    client: QdrantClient,
    model: SentenceTransformer,
    question: str,
    top_k: int = 3,
) -> list[Any]:
    """Search Qdrant for the most relevant chunks."""

    query_vector = model.encode(question, normalize_embeddings=True).tolist()

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
    )

    return response.points


def print_search_results(question: str, results: list[Any]) -> None:
    """Print retrieval results in a readable format."""
    print("\n" + "=" * 80)
    print(f"QUESTION: {question}")
    print("=" * 80)

    for index, result in enumerate(results, start=1):
        payload = result.payload or {}

        print(f"\nResult {index}")
        print(f"Score    : {result.score:.4f}")
        print(f"Source   : {payload.get('source')}")
        print(f"Page     : {payload.get('page')}")
        print(f"Section  : {payload.get('section')}")
        print(f"Chunk ID : {payload.get('chunk_id')}")
        print("Text     :")
        print(payload.get("text"))


def search_documents(
    query: str,
    limit: int = 5,
) -> list[Any]:
    """
    Search the persisted Qdrant collection.

    Used by Day 16 RAG service.
    """

    return search_chunks(
        client=qdrant_client,
        model=model,
        question=query,
        top_k=limit,
    )


def initialize_vector_database() -> None:
    """
    Build the vector database if it does not exist.

    Safe to run multiple times.
    """

    if qdrant_client.collection_exists(collection_name=COLLECTION_NAME):
        return

    chunks = build_chunks(DATA_DIR)

    create_qdrant_collection(qdrant_client)

    upsert_chunks(
        client=qdrant_client,
        model=model,
        chunks=chunks,
    )


def main() -> None:
    """Run the Day 15 vector database demo."""

    initialize_vector_database()

    test_questions = [
        "What is RAG?",
        "Why is RAG useful?",
        "What are the components of a RAG system?",
        "What is FastAPI used for?",
        "How does FastAPI validate data?",
        "What is Swagger UI?",
        "What does an AI engineer do?",
        "Why should AI apps be testable?",
        "What is retrieval augmented generation?",
        "Which documents talk about APIs?",
    ]

    for question in test_questions:
        results = search_chunks(
            client=qdrant_client,
            model=model,
            question=question,
            top_k=3,
        )

        print_search_results(
            question=question,
            results=results,
        )


if __name__ == "__main__":
    try:
        main()
    finally:
        qdrant_client.close()
