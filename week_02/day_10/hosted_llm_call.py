import os

from dotenv import load_dotenv
from openai import OpenAI


def get_client() -> OpenAI:
    """
    Create and return an OpenAI client.

    The client reads the API key from the OPENAI_API_KEY environment variable.
    """

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to your .env file or shell environment."
        )

    return OpenAI(api_key=api_key)


def call_hosted_llm(prompt: str) -> str:
    """
    Send a prompt to a hosted OpenAI model and return the text response.
    """

    client = get_client()

    model = os.getenv("OPENAI_MODEL", "gpt-5.5")

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text


def main() -> None:
    """
    Run a small hosted LLM example.
    """

    prompt = """
    Explain the difference between hosted API models and open-weight models
    in 5 beginner-friendly bullet points.
    """

    result = call_hosted_llm(prompt)

    print("\nHosted LLM Response")
    print("-------------------")
    print(result)


if __name__ == "__main__":
    main()
