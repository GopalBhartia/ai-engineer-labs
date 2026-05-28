from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset


class PointsDataset(Dataset):
    """
    A tiny custom dataset.

    Each sample is a 2D point: [x1, x2]

    Label rule:
    - If x1 + x2 > 0, label is 1
    - Otherwise, label is 0
    """

    def __init__(self, num_samples: int = 1000) -> None:
        super().__init__()

        self.features = torch.randn(num_samples, 2)

        sums = self.features[:, 0] + self.features[:, 1]
        self.labels = (sums > 0).long()

    def __len__(self) -> int:
        return len(self.features)

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        return self.features[index], self.labels[index]


class TinyClassifier(nn.Module):
    """
    A tiny neural network for binary classification.

    Input:
    - 2 numbers: x1 and x2

    Output:
    - 2 logits: one score for class 0, one score for class 1
    """

    def __init__(self) -> None:
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, 2),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


def train_model(
    model: nn.Module,
    dataloader: DataLoader,
    loss_fn: nn.Module,
    optimizer: torch.optim.Optimizer,
    epochs: int = 20,
) -> None:
    """
    Train the model using a standard PyTorch training loop.
    """

    model.train()

    for epoch in range(epochs):
        total_loss = 0.0
        correct_predictions = 0
        total_predictions = 0

        for features, labels in dataloader:
            # 1. Forward pass: model makes predictions
            logits = model(features)

            # 2. Calculate loss: how wrong the model is
            loss = loss_fn(logits, labels)

            # 3. Clear old gradients
            optimizer.zero_grad()

            # 4. Backward pass: calculate gradients
            loss.backward()

            # 5. Update model weights
            optimizer.step()

            total_loss += loss.item()

            predicted_labels = logits.argmax(dim=1)
            correct_predictions += (predicted_labels == labels).sum().item()
            total_predictions += labels.size(0)

        average_loss = total_loss / len(dataloader)
        accuracy = correct_predictions / total_predictions

        print(
            f"Epoch {epoch + 1:02d}/{epochs} | "
            f"Loss: {average_loss:.4f} | "
            f"Accuracy: {accuracy:.4f}"
        )


def evaluate_model(model: nn.Module, dataloader: DataLoader) -> None:
    """
    Evaluate the model after training.
    """

    model.eval()

    correct_predictions = 0
    total_predictions = 0

    with torch.no_grad():
        for features, labels in dataloader:
            logits = model(features)
            predicted_labels = logits.argmax(dim=1)

            correct_predictions += (predicted_labels == labels).sum().item()
            total_predictions += labels.size(0)

    accuracy = correct_predictions / total_predictions
    print(f"\nFinal Evaluation Accuracy: {accuracy:.4f}")


def save_model(model: nn.Module, path: Path) -> None:
    """
    Save only the model weights.

    This is the recommended beginner-friendly way:
    save the state_dict, not the full model object.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), path)
    print(f"\nModel weights saved to: {path}")


def load_model(path: Path) -> TinyClassifier:
    """
    Load model weights into a fresh model instance.
    """

    model = TinyClassifier()
    model.load_state_dict(torch.load(path))
    model.eval()

    print(f"Model weights loaded from: {path}")

    return model


def test_loaded_model(model: nn.Module) -> None:
    """
    Test the loaded model on a few custom points.
    """

    test_points = torch.tensor(
        [
            [2.0, 1.0],  # sum = 3, expected class 1
            [-2.0, -1.0],  # sum = -3, expected class 0
            [1.0, -3.0],  # sum = -2, expected class 0
            [-1.0, 3.0],  # sum = 2, expected class 1
        ]
    )

    with torch.no_grad():
        logits = model(test_points)
        predictions = logits.argmax(dim=1)

    print("\nPredictions from loaded model:")

    for point, prediction in zip(test_points, predictions, strict=True):
        print(f"Point: {point.tolist()} => Predicted class: {prediction.item()}")


def main() -> None:
    torch.manual_seed(42)

    dataset = PointsDataset(num_samples=1000)

    train_size = int(0.8 * len(dataset))
    test_size = len(dataset) - train_size

    train_dataset, test_dataset = torch.utils.data.random_split(
        dataset,
        [train_size, test_size],
    )

    train_dataloader = DataLoader(
        train_dataset,
        batch_size=32,
        shuffle=True,
    )

    test_dataloader = DataLoader(
        test_dataset,
        batch_size=32,
        shuffle=False,
    )

    model = TinyClassifier()

    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=0.1,
    )

    train_model(
        model=model,
        dataloader=train_dataloader,
        loss_fn=loss_fn,
        optimizer=optimizer,
        epochs=20,
    )

    evaluate_model(
        model=model,
        dataloader=test_dataloader,
    )

    model_path = Path("week_02/day_08/tiny_classifier_weights.pth")

    save_model(
        model=model,
        path=model_path,
    )

    loaded_model = load_model(model_path)

    test_loaded_model(loaded_model)


if __name__ == "__main__":
    main()
