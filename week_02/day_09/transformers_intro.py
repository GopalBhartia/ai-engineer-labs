from transformers import AutoTokenizer, pipeline


def run_sentiment_pipeline() -> None:
    """
    Run a pretrained Hugging Face sentiment-analysis pipeline.
    """

    classifier = pipeline(
        task="sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
    )

    texts = [
        "I love learning about transformers and LLMs.",
        "This error is frustrating and difficult to debug.",
        "The course is okay, but I expected more practical examples.",
    ]

    results = classifier(texts)

    print("\nSentiment Analysis Results")
    print("--------------------------")

    for text, result in zip(texts, results, strict=True):
        print(f"Text : {text}")
        print(f"Label: {result['label']}")
        print(f"Score: {result['score']:.4f}")
        print()


def inspect_tokenizer_output() -> None:
    """
    Inspect how a tokenizer converts text into tokens and token IDs.
    """

    model_name = "distilbert-base-uncased-finetuned-sst-2-english"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    text = "Transformers convert text into tokens before the model reads it."

    encoded = tokenizer(text)

    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    print("\nTokenizer Inspection")
    print("--------------------")

    print(f"Original text:\n{text}\n")

    print("Tokens:")
    print(tokens)

    print("\nToken IDs:")
    print(token_ids)

    print("\nFull encoded output:")
    print(encoded)

    print(f"\nNumber of tokens without special tokens: {len(tokens)}")
    print(f"Number of input IDs with special tokens: {len(encoded['input_ids'])}")


def compare_token_counts() -> None:
    """
    Compare token counts for different types of text.
    """

    model_name = "distilbert-base-uncased-finetuned-sst-2-english"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    examples = [
        "AI is useful.",
        "Artificial intelligence is transforming software engineering.",
        "Supercalifragilisticexpialidocious is a very unusual word.",
        "नमस्ते, मैं आज Transformers सीख रहा हूँ।",
    ]

    print("\nToken Count Comparison")
    print("----------------------")

    for text in examples:
        tokens = tokenizer.tokenize(text)

        print(f"Text       : {text}")
        print(f"Tokens     : {tokens}")
        print(f"Token count: {len(tokens)}")
        print()


def main() -> None:
    run_sentiment_pipeline()
    inspect_tokenizer_output()
    compare_token_counts()


if __name__ == "__main__":
    main()
