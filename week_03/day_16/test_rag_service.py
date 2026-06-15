from week_03.day_16.rag_service import answer_question


def main() -> None:
    response = answer_question("What is FastAPI?")

    print(response.model_dump())


if __name__ == "__main__":
    main()
