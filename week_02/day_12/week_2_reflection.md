# Week 2 Reflection

## What I learned this week

This week focused on the foundations needed to build reliable AI and LLM applications.

I learned that modern AI engineering is not only about calling an LLM API. It also requires understanding machine learning basics, evaluation, tokenization, model selection, prompt design, testing, and clean software structure.

## Day 7: ML Workflow

I learned the basic machine learning workflow:

- Prepare a dataset.
- Split data into training and test sets.
- Train a baseline model.
- Evaluate the model using metrics.
- Understand overfitting and underfitting.

Important metrics I practiced:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Key takeaway:

A model should not be judged only by accuracy. Different metrics matter depending on the use case.

## Day 8: PyTorch Essentials

I learned the basic PyTorch training flow:

- Create tensors.
- Build a dataset.
- Use DataLoader.
- Define a model.
- Define a loss function.
- Use an optimizer.
- Run a training loop.
- Save and load model weights.

Key takeaway:

Training a neural network is an iterative process where the model makes predictions, calculates error, and updates weights using backpropagation and gradient descent.

## Day 9: Transformers and Tokenization

I learned that LLMs do not directly process words the way humans do. They process tokens.

A token can be:

- A word
- Part of a word
- A symbol
- A punctuation mark
- A space-like text unit

I also learned that context windows and token costs matter because longer prompts use more tokens, increase cost, and may affect latency.

Key takeaway:

Good AI engineers must think about prompt size, context limits, and cost efficiency.

## Day 10: LLM Lifecycle and Model Selection

I learned that building LLM applications involves a lifecycle:

- Define the problem.
- Choose the model.
- Design prompts.
- Evaluate outputs.
- Deploy the app.
- Monitor quality, cost, and latency.

I also compared hosted APIs and open-weight models.

Hosted APIs are easier to use and maintain, but may involve cost, rate limits, and privacy considerations.

Open-weight models provide more control and privacy options, but require more infrastructure and deployment work.

Key takeaway:

Model selection should be based on cost, latency, quality, privacy, and operational complexity.

## Day 11: Prompt Engineering for Developers

I learned prompt engineering concepts such as:

- Clear instructions
- Input/output format
- Examples
- Constraints
- Structured outputs
- Prompt regression testing

I also built reusable prompt templates and tests.

Key takeaway:

Prompt engineering is not just writing clever prompts. It is about creating repeatable, testable, and reliable instructions for LLM-powered systems.

## Day 12: Weekly Integration Lab

I wrapped an LLM call behind a Python service class.

The service class gives the project a cleaner structure because the rest of the app does not need to know the details of the model provider.

I also added:

- A model client protocol
- A mock model client
- A structured LLM response object
- Token and cost logging placeholders
- Unit tests with fake model output

Key takeaway:

LLM calls should be wrapped behind clean interfaces so they are easier to test, replace, and maintain.

## Biggest lesson from Week 2

The biggest lesson is that AI engineering combines machine learning knowledge with strong software engineering.

It is not enough to know how to call an LLM. A good AI engineer must also know how to:

- Structure code cleanly
- Test model behavior
- Track usage and cost
- Compare model options
- Design prompts carefully
- Evaluate output quality
- Build maintainable systems

## What I want to improve next

In the next weeks, I want to improve at:

- Building retrieval-augmented generation systems
- Working with embeddings and vector databases
- Evaluating LLM outputs more systematically
- Creating production-ready AI APIs
- Improving testing strategies for LLM applications