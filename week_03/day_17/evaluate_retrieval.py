from __future__ import annotations

from week_03.day_15.vector_db_demo import search_documents
from week_03.day_17.golden_dataset import GOLDEN_DATASET


def evaluate_retrieval() -> None:
    total_questions = len(GOLDEN_DATASET)
    hits = 0

    print("\nRetrieval Evaluation")
    print("=" * 80)

    for item in GOLDEN_DATASET:
        question = item["question"]
        expected_source = item["expected_source"]

        results = search_documents(question)

        retrieved_sources = {result.payload.get("source") for result in results}

        hit = expected_source in retrieved_sources

        if hit:
            hits += 1

        print(f"\nQuestion: {question}")
        print(f"Expected: {expected_source}")
        print(f"Retrieved: {sorted(retrieved_sources)}")
        print(f"Result: {'HIT' if hit else 'MISS'}")

    hit_rate = hits / total_questions

    print("\n" + "=" * 80)
    print(f"Hits: {hits}/{total_questions}")
    print(f"Hit Rate: {hit_rate:.2%}")
    print("=" * 80)


if __name__ == "__main__":
    evaluate_retrieval()
