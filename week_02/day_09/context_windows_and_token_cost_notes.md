# Day 9 Notes: Transformers, Tokenization, Context Windows, and Token Cost

## 1. What Is a Token?

A token is a piece of text that a language model processes.

A token can be:

- A full word
- Part of a word
- A punctuation mark
- A number
- A symbol
- A space plus a word, depending on the tokenizer

Models do not read raw text directly. They read token IDs.

Example:

```text
Text: I love AI
Tokens: ["I", "love", "AI"]
Token IDs: [some_number, some_number, some_number]
```

The exact tokens and token IDs depend on the tokenizer used by the model.

---

## 2. What Is Tokenization?

Tokenization is the process of converting text into tokens and then converting those tokens into numeric token IDs.

The basic flow is:

```text
Raw text
-> tokens
-> token IDs
-> model input
```

Tokenization matters because the model's context window, speed, and cost are usually measured in tokens, not words.

---

## 3. Why Subword Tokenization Is Used

Modern Transformer models usually do not split text only by words.

They often use subword tokenization.

This means rare or complex words can be broken into smaller pieces.

Example:

```text
unbelievable
-> un + believ + able
```

This helps the model handle:

- Rare words
- New words
- Names
- Technical terms
- Misspellings
- Multiple languages

Subword tokenization keeps the vocabulary smaller while still allowing the model to represent many possible words.

---

## 4. What Are Token IDs?

After text is split into tokens, each token is converted into a number.

Example:

```text
Tokens: ["AI", "is", "useful"]
Token IDs: [20185, 318, 4465]
```

The model receives these numbers as input.

The numbers are indexes into the model's vocabulary.

---

## 5. What Are Embeddings?

Token IDs are converted into dense numeric vectors called embeddings.

An embedding represents a token in a mathematical form.

Tokens with similar meanings often have similar embeddings.

Example:

```text
"king" and "queen" may have related embeddings.
"car" and "banana" may have less related embeddings.
```

Embeddings help the model work with meaning rather than raw text.

---

## 6. What Is Attention?

Attention is the mechanism that allows a Transformer model to decide which tokens are important for understanding other tokens.

Example:

```text
The animal did not cross the road because it was tired.
```

The model uses attention to connect `"it"` with `"animal"`.

Attention helps models understand relationships between words even when the words are far apart in the sentence.

---

## 7. What Is Self-Attention?

Self-attention means every token in a sequence can look at other tokens in the same sequence.

Example sentence:

```text
The cat sat on the mat.
```

The token `"cat"` can attend to:

- `"The"`
- `"sat"`
- `"on"`
- `"mat"`

This helps the model understand the full context of each token.

The same word can have different meanings depending on context.

Example:

```text
I deposited money in the bank.
I sat near the river bank.
```

The word `"bank"` means different things in these two sentences.

Self-attention helps the model understand that difference.

---

## 8. What Is a Transformer?

A Transformer is a neural network architecture based heavily on attention.

Transformers are the foundation of many modern NLP and LLM systems.

They are better than older sequence models for many language tasks because they can look at many tokens together instead of processing text only one token at a time.

Common Transformer types:

- Encoder-only models
- Decoder-only models
- Encoder-decoder models

---

## 9. Encoder-Only Models

Encoder-only models are good for understanding text.

Examples:

```text
BERT
DistilBERT
RoBERTa
```

Common tasks:

- Sentiment analysis
- Text classification
- Named entity recognition
- Semantic search
- Embedding generation

Example:

```text
Input: This movie was excellent.
Output: POSITIVE
```

---

## 10. Decoder-Only Models

Decoder-only models are good for generating text.

Examples:

```text
GPT-style models
LLaMA-style models
Mistral-style models
```

Common tasks:

- Chatbots
- Text completion
- Code generation
- Agent reasoning
- Creative writing

Example:

```text
Input: Once upon a time
Output: there was a small village...
```

---

## 11. Encoder-Decoder Models

Encoder-decoder models are good for converting one text into another text.

Examples:

```text
T5
BART
Flan-T5
```

Common tasks:

- Translation
- Summarization
- Question answering
- Instruction following

Example:

```text
Input: Translate English to French: Good morning
Output: Bonjour
```

---

## 12. What Is Pretraining?

Pretraining is the first large training stage.

A model is trained on a huge amount of general text.

During pretraining, the model learns:

- Grammar
- Language patterns
- Facts
- Common reasoning patterns
- Word relationships
- Sentence structure

For many language models, pretraining involves predicting missing words or predicting the next token.

Example:

```text
Input: The capital of India is
Target: Delhi
```

Pretraining gives the model general language ability.

---

## 13. What Is Fine-Tuning?

Fine-tuning happens after pretraining.

A pretrained model is trained further on a smaller, task-specific dataset.

Examples:

- Sentiment classification
- Customer support chatbot
- Legal document summarization
- Medical question answering
- Code generation
- Resume screening

Pretraining gives the model general knowledge.

Fine-tuning adapts the model to a specific task.

---

## 14. What Is Inference?

Inference means using a trained model to make predictions.

Example:

```text
Input: I love this product!
Output: POSITIVE
```

During inference, the model is not learning new weights.

It is only using its existing trained weights to produce an output.

In Day 9, we used pretrained models for inference.

---

## 15. What Is a Hugging Face Pipeline?

A Hugging Face pipeline is a simple high-level API for using pretrained models.

It hides many internal steps.

When we call a pipeline, it usually handles:

```text
Raw text
-> tokenization
-> token IDs
-> model inference
-> output processing
-> readable result
```

Example:

```python
classifier = pipeline("sentiment-analysis")
result = classifier("I love learning about AI.")
```

The pipeline makes it easy to use models without manually writing all preprocessing and postprocessing code.

---

## 16. What Is a Context Window?

A context window is the maximum amount of text a model can consider at one time.

It is usually measured in tokens.

Example:

```text
Context window: 4,096 tokens
```

This means the model can process up to 4,096 tokens in one request.

The context window includes:

- User prompt
- System message
- Conversation history
- Retrieved documents
- Tool outputs
- Model's generated response

If the input is too long, some text must be removed, shortened, summarized, or chunked.

---

## 17. Why Context Windows Matter

Context windows matter because an LLM cannot use information it cannot see.

If important information is outside the context window, the model may:

- Forget earlier details
- Miss important instructions
- Give incomplete answers
- Hallucinate
- Use outdated or irrelevant context

For RAG systems, context windows are especially important because retrieved chunks must fit inside the available context.

---

## 18. What Is Token Cost?

Many LLM APIs charge based on token usage.

Usually, both input tokens and output tokens count.

Example:

```text
Input tokens: 2,000
Output tokens: 500
Total tokens: 2,500
```

Token cost matters because longer prompts and longer outputs cost more.

---

## 19. Why Token Cost Matters in AI Apps

Token cost affects:

- API bills
- Latency
- Scalability
- User experience
- Prompt design
- RAG chunking strategy
- Conversation memory design

A small prototype may work fine with long prompts.

But in production, sending too many tokens for every request can become slow and expensive.

---

## 20. Context Window vs Token Cost

A larger context window allows the model to see more information.

But larger context usage can also increase cost and latency.

Good AI engineers balance:

- Enough context for quality
- Not too much context to waste money
- Clear instructions
- Relevant retrieved chunks
- Shorter outputs when possible

---

## 21. Practical Tips for AI Engineers

Use short, clear prompts.

Only include relevant context.

For RAG, retrieve the most useful chunks instead of sending entire documents.

Summarize older conversation history.

Avoid repeatedly sending unnecessary examples.

Track token counts during development.

Choose the right model for the job.

Use smaller or cheaper models for simple tasks.

Use larger models only when the task requires stronger reasoning.

---

## 22. Simple Mental Model

The model does not think in words.

It processes tokens.

The flow is:

```text
Text
-> tokens
-> token IDs
-> embeddings
-> Transformer layers
-> output
```

So as an AI engineer, I should always think about:

```text
How many tokens am I sending?
Is the important context included?
Am I wasting tokens?
Will this fit inside the model's context window?
How much will this cost at scale?
```

---

## 23. Day 9 Summary

Today I learned that:

- Tokens are the basic units processed by language models.
- Tokenizers convert text into token IDs.
- Embeddings convert token IDs into meaningful vectors.
- Attention helps the model understand relationships between tokens.
- Transformers are neural networks built around attention.
- Encoder-only models are good for understanding tasks.
- Decoder-only models are good for generation tasks.
- Encoder-decoder models are good for text-to-text tasks.
- Pretraining gives a model general language ability.
- Fine-tuning adapts a pretrained model to a specific task.
- Hugging Face pipelines make it easy to use pretrained models.
- Context windows define how much text a model can process at once.
- Token cost affects API bills, latency, and production scalability.