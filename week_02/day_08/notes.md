## Day 8 - PyTorch Essentials Notes

### Overview

Today I learned the basic PyTorch workflow for training a tiny neural network.

The main goal was to understand how these pieces connect together:

1. Tensors
2. Dataset
3. DataLoader
4. Model
5. Loss function
6. Optimizer
7. Training loop
8. Evaluation
9. Saving model weights
10. Loading model weights

---

## 1. What is a Tensor?

A tensor is the main data structure used in PyTorch.

A tensor is like a container for numbers.

Examples:

- A single number is a 0D tensor.
- A list of numbers is a 1D tensor.
- A table of numbers is a 2D tensor.
- An image can be represented as a 3D tensor.

In machine learning, tensors are used to store:

- Input data
- Labels
- Model weights
- Predictions
- Loss values
- Gradients

Example from the Day 8 project:

    self.features = torch.randn(num_samples, 2)

This creates random 2D points.

The shape is:

    [1000, 2]

This means:

- 1000 training examples
- 2 input values per example

---

## 2. What is a Dataset?

A Dataset stores the training examples.

In PyTorch, a custom dataset usually defines two important methods:

    def len(self):
        return number_of_examples

    def getitem(self, index):
        return one_feature, one_label

The __len__ method tells PyTorch how many examples are in the dataset.

The __getitem__ method tells PyTorch how to fetch one example.

In the Day 8 project, each example was a 2D point.

Example:

    [0.5, 1.2]

The label was created using this rule:

    If x1 + x2 > 0, label = 1
    Otherwise, label = 0

So the model learned to classify points into two classes.

---

## 3. What is a DataLoader?

A DataLoader takes a Dataset and gives data to the model in batches.

Instead of giving the model one example at a time, it gives a group of examples.

Example:

    DataLoader(dataset, batch_size=32, shuffle=True)

This means:

- Use 32 examples at a time.
- Shuffle the training data before training.

Batching is useful because:

- Training becomes faster.
- Updates become more stable.
- The model sees data in smaller groups instead of all at once.

---

## 4. What is a Model in PyTorch?

A model is a function that takes input data and produces predictions.

In PyTorch, models usually inherit from nn.Module.

Example:

    class TinyClassifier(nn.Module):
        def init(self):
            super().init()

            self.network = nn.Sequential(
                nn.Linear(2, 8),
                nn.ReLU(),
                nn.Linear(8, 2),
            )

        def forward(self, x):
            return self.network(x)

This model has:

- 2 input values
- 1 hidden layer with 8 neurons
- ReLU activation
- 2 output scores

The two output scores are called logits.

The logits represent:

- Score for class 0
- Score for class 1

The class with the higher score becomes the model's prediction.

---

## 5. What is Loss?

Loss measures how wrong the model is.

If the model prediction is very wrong, the loss is high.

If the model prediction is close to correct, the loss is low.

In the Day 8 project, I used:

    loss_fn = nn.CrossEntropyLoss()

CrossEntropyLoss is commonly used for classification problems.

The goal of training is to reduce the loss over time.

---

## 6. What is an Optimizer?

An optimizer updates the model weights.

The model starts with random weights.

At the beginning, predictions are usually bad.

The optimizer slowly changes the weights so that the model makes better predictions.

In the Day 8 project, I used:

    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

SGD means Stochastic Gradient Descent.

The learning rate controls how big each update should be.

In this example:

    lr=0.1

A learning rate that is too small can make training slow.

A learning rate that is too large can make training unstable.

---

## 7. Gradient Descent Intuition

Gradient descent is the process of improving the model step by step.

Imagine standing on a hill and trying to walk down to the lowest point.

You look at the slope and take a small step downward.

In machine learning:

- The hill is the loss function.
- The height is the loss value.
- The lowest point is the best model.
- The slope is the gradient.
- Each step changes the model weights.

The basic idea is:

    Bad prediction
    -> high loss
    -> calculate gradients
    -> update weights
    -> better prediction

This process repeats many times during training.

---

## 8. Backpropagation Intuition

Backpropagation is how the model figures out which weights caused the error.

First, the model makes a prediction.

Then the loss function calculates how wrong the prediction was.

Backpropagation sends this error backward through the network.

It calculates how much each weight contributed to the mistake.

In PyTorch, this happens with:

    loss.backward()

This calculates gradients for the model parameters.

A gradient answers this question:

    If this weight changes slightly, how will the loss change?

After gradients are calculated, the optimizer updates the weights:

    optimizer.step()

---

## 9. The PyTorch Training Loop

The most important PyTorch pattern is:

    logits = model(features)
    loss = loss_fn(logits, labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

This means:

1. Make predictions.
2. Calculate the error.
3. Clear old gradients.
4. Calculate new gradients.
5. Update model weights.

This pattern is the heart of most PyTorch training workflows.

---

## 10. Why do we use optimizer.zero_grad()?

PyTorch accumulates gradients by default.

This means gradients from the previous batch can remain in memory.

If we do not clear old gradients, they get added to the new gradients.

That can make training incorrect.

So before calculating new gradients, we use:

    optimizer.zero_grad()

This makes sure each training step uses only the gradients from the current batch.

---

## 11. Why do we use model.train()?

We use:

    model.train()

before training.

This tells PyTorch that the model is in training mode.

Some layers behave differently during training and evaluation.

Examples:

- Dropout
- Batch normalization

Even though the Day 8 tiny model does not use these layers, using model.train() is still a good habit.

---

## 12. Why do we use model.eval()?

We use:

    model.eval()

before evaluation or inference.

This tells PyTorch that the model is not being trained.

The model should only make predictions.

During evaluation, we also use:

    with torch.no_grad():

This tells PyTorch not to track gradients.

This is useful because:

- It saves memory.
- It makes prediction faster.
- It avoids unnecessary gradient calculations.

---

## 13. Saving Model Weights

Model weights are the learned parameters of the neural network.

After training, I saved the model weights using:

    torch.save(model.state_dict(), path)

This saves only the learned weights.

It does not save the entire Python class.

Saving only the state_dict is a common and clean approach.

---

## 14. Loading Model Weights

To load saved weights, we first create the same model structure again:

    model = TinyClassifier()

Then we load the saved weights:

    model.load_state_dict(torch.load(path))

Then we put the model in evaluation mode:

    model.eval()

This allows us to reuse the trained model later without training it again from scratch.

---

## 15. Day 8 Summary

Today I learned the basic PyTorch training workflow.

I built a tiny neural network that classifies 2D points into two classes.

The model learned this rule:

    If x1 + x2 > 0, class = 1
    Otherwise, class = 0

The main PyTorch workflow was:

1. Create a dataset.
2. Load data using DataLoader.
3. Define a neural network using nn.Module.
4. Choose a loss function.
5. Choose an optimizer.
6. Run a training loop.
7. Evaluate the model.
8. Save model weights.
9. Load model weights.
10. Test predictions from the loaded model.

The most important code pattern from today was:

    logits = model(features)
    loss = loss_fn(logits, labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

This is the core pattern behind most deep learning training workflows.