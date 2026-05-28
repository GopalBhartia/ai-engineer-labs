from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def load_dataset() -> tuple[list[str], list[int], list[str]]:
    """Load a simple real-world text classification dataset."""

    categories = ["sci.space", "rec.sport.baseball"]

    dataset = fetch_20newsgroups(
        subset="all",
        categories=categories,
        remove=("headers", "footers", "quotes"),
    )

    texts = list(dataset.data)
    labels = list(dataset.target)
    target_names = list(dataset.target_names)

    return texts, labels, target_names


def train_model() -> None:
    """Train and evaluate a simple text classification model."""

    texts, labels, target_names = load_dataset()

    x_train, x_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.25,
        random_state=42,
        stratify=labels,
    )

    model = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    stop_words="english",
                    max_features=5000,
                ),
            ),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0,
    )
    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0,
    )

    print("Model Evaluation")
    print("----------------")
    print(f"Accuracy : {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall   : {recall:.2f}")
    print()

    print("Classification Report")
    print("---------------------")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=target_names,
            zero_division=0,
        )
    )

    matrix = confusion_matrix(y_test, predictions)

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=target_names,
    )

    display.plot()
    plt.title("Text Classification Confusion Matrix")

    output_dir = Path("week_02/day_07/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "confusion_matrix.png"
    plt.savefig(output_path)

    print(f"Confusion matrix saved to: {output_path}")


if __name__ == "__main__":
    train_model()
