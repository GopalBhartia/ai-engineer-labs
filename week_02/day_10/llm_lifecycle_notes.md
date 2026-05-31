# Day 10 Notes: LLM Lifecycle and Model Selection

## 1. What Is the GenAI Lifecycle?

The GenAI lifecycle is the full process of building, testing, deploying, and improving a generative AI application.

It is not only about calling an LLM API.

A real GenAI lifecycle looks like this:

```text
Problem definition
-> Data
-> Model selection
-> Prompting
-> Evaluation
-> Safety
-> Deployment
-> Monitoring
-> Improvement
```

Each stage matters because AI applications can fail in many ways:

- Wrong model choice
- Poor prompt design
- Bad retrieval
- Hallucinations
- High cost
- Slow latency
- Privacy issues
- Unsafe outputs
- Weak evaluation
- Poor monitoring

---

## 2. Problem Definition

Before choosing a model, we must define the problem clearly.

A vague problem statement is:

```text
Build an AI chatbot.
```

A better problem statement is:

```text
Build a customer-support assistant that answers refund-policy questions from company documents and escalates uncertain cases to a human.
```

The better version tells us:

- Who the user is
- What the task is
- What data is needed
- What the expected behavior is
- What should happen when the model is uncertain

Good problem definition makes model selection and evaluation easier.

---

## 3. Data in the LLM Lifecycle

Data is one of the most important parts of a GenAI system.

Data can include:

- User prompts
- System prompts
- Conversation history
- Retrieved documents
- Tool outputs
- Fine-tuning datasets
- Evaluation datasets
- User feedback
- Logs
- Safety examples

In many modern GenAI apps, we do not train a model from scratch.

Instead, we usually use:

- Prompting
- Retrieval-Augmented Generation
- Tool calling
- Structured outputs
- Fine-tuning only when needed

---

## 4. What Is RAG?

RAG means Retrieval-Augmented Generation.

In RAG, the system retrieves relevant information from a knowledge source and gives it to the model as context.

Example:

```text
User asks: What is the refund policy?

System retrieves: refund_policy.pdf, section 3

Model answers: According to the refund policy, customers can request a refund within 30 days.
```

RAG is useful because the model does not need to memorize all private or changing information.

Instead, it can answer using retrieved context.

RAG is commonly used for:

- Company knowledge assistants
- Document question answering
- Legal document search
- Support bots
- Internal tools
- Research assistants

---

## 5. Model Selection

Model selection means choosing the right model for the task.

A bigger model is not always the best model.

The right model depends on:

- Quality requirements
- Cost limits
- Latency requirements
- Privacy needs
- Context window size
- Tool/function calling support
- Structured output support
- Reasoning ability
- Coding ability
- Deployment complexity
- Evaluation results

For simple tasks, a smaller model may be enough.

For complex reasoning tasks, a stronger model may be required.

---

## 6. Important Model Selection Factors

### Quality

Quality means how good the model output is.

Good quality can mean:

- Accurate answers
- Clear writing
- Correct reasoning
- Less hallucination
- Good instruction following
- Good formatting
- Reliable tool use

### Cost

Cost means how expensive the model is to use.

Many hosted LLM APIs charge based on tokens.

Both input tokens and output tokens can affect cost.

A long prompt with a long response usually costs more than a short prompt with a short response.

### Latency

Latency means how long the model takes to respond.

Low latency is important for:

- Chat apps
- Customer support
- Voice agents
- Real-time copilots
- Interactive tools

A stronger model may give better answers but may also be slower.

### Privacy

Privacy means how sensitive the data is and where it is processed.

For private data, we need to think carefully about:

- Whether data leaves our infrastructure
- Provider data policies
- Logging
- Retention
- Compliance
- Encryption
- Access control

### Context Window

The context window is the maximum amount of text the model can process at once.

It is measured in tokens.

The context window includes:

- System prompt
- User prompt
- Conversation history
- Retrieved documents
- Tool results
- Model output

Large context windows are useful for long documents, but they can increase cost and latency.

### Tool Support

Some models are better at using tools or function calling.

Tool support matters for agentic AI systems.

Examples:

- Search tool
- Calculator tool
- Database tool
- Calendar tool
- Email tool
- Code execution tool

### Structured Output

Structured output means making the model return data in a fixed format.

Example:

```json
{
  "sentiment": "positive",
  "urgency": "low",
  "department": "support"
}
```

Structured output is useful when the model response must be consumed by another program.

---

## 7. Hosted API Models

A hosted API model is a model served by a provider.

Examples of hosted API providers include:

- OpenAI
- Anthropic
- Google
- Mistral
- Cohere
- Groq
- Together
- Fireworks

With a hosted API model, we send a request to the provider and receive a response.

The provider manages:

- Model hosting
- GPU infrastructure
- Scaling
- Reliability
- Updates
- Optimization

### Advantages of Hosted API Models

Hosted API models are useful because they are easy to start with.

Advantages:

- Fast setup
- No GPU required
- High-quality models
- Easy scaling
- Good for prototypes
- Good for production apps
- Less infrastructure work
- Usually strong documentation

### Disadvantages of Hosted API Models

Disadvantages:

- Usage-based cost
- External dependency
- Rate limits
- Less control over model internals
- Data privacy concerns
- Possible vendor lock-in
- Model behavior can change over time
- Requires internet/API availability

---

## 8. Open-Weight Models

An open-weight model is a model where the model weights are available.

Examples include many models from families such as:

- Llama
- Mistral open models
- Qwen
- Gemma
- DeepSeek open models

Open-weight models can be run:

- Locally
- On private servers
- On cloud GPUs
- Through inference providers

### Advantages of Open-Weight Models

Advantages:

- More control
- Better privacy options
- Can run on your own infrastructure
- Can fine-tune deeply
- Less provider lock-in
- Can be cheaper at very large scale
- Useful for private enterprise workloads

### Disadvantages of Open-Weight Models

Disadvantages:

- Harder to deploy
- Requires infrastructure knowledge
- May need GPUs
- Scaling is your responsibility
- Monitoring is your responsibility
- Security is your responsibility
- Latency optimization is your responsibility
- Quality may be lower than top hosted frontier models

---

## 9. Hosted API vs Open-Weight Models

| Factor | Hosted API Model | Open-Weight Model |
|---|---|---|
| Setup speed | Very fast | Slower |
| Infrastructure | Provider manages it | You manage it |
| Quality | Often very high | Depends on model |
| Cost | Pay per usage | Infra cost |
| Privacy | Depends on provider | More control |
| Customization | Limited to provider options | More control |
| Scaling | Easier | Harder |
| Maintenance | Easier | Harder |
| Best for | Fast development and high quality | Privacy, control, custom deployment |

---

## 10. When to Use Hosted API Models

Use a hosted API model when:

- You want to move fast
- You are building a prototype
- You do not want to manage GPUs
- You need high-quality responses
- Your usage is moderate
- You want easier deployment
- You want strong tool-calling support
- You are still experimenting with the product

Example:

```text
A startup building an MVP for a customer-support assistant may start with a hosted API model.
```

---

## 11. When to Use Open-Weight Models

Use an open-weight model when:

- Privacy is critical
- You need full control
- You want to run the model on your own infrastructure
- You want to avoid provider lock-in
- You have high usage and can optimize infrastructure
- You need deep customization
- You have the engineering skills to manage deployment

Example:

```text
A financial company handling sensitive internal documents may consider open-weight models deployed inside private infrastructure.
```

---

## 12. Prompting in the LLM Lifecycle

Prompting means giving instructions to the model.

A prompt may include:

- Role
- Task
- Context
- Constraints
- Examples
- Output format
- Safety rules

Weak prompt:

```text
Summarize this.
```

Better prompt:

```text
Summarize the following customer complaint in 5 bullet points.
Include the product name, issue, customer sentiment, requested resolution, and urgency level.
Return the answer as valid JSON.
```

Good prompting improves:

- Accuracy
- Format consistency
- Reliability
- User experience

---

## 13. Evaluation

Evaluation means testing whether the AI system works correctly.

A common beginner mistake is trying one example and assuming the model is good.

Production AI systems need systematic evaluation.

We should test:

- Accuracy
- Hallucination rate
- Formatting correctness
- Tool usage
- Latency
- Cost
- Safety
- Edge cases
- Long inputs
- Bad inputs
- Multilingual inputs

Example evaluation item:

```text
Question: What is the refund period?
Expected answer: 30 days
Source document: refund_policy_v2.pdf
Pass condition: The answer must mention 30 days and must not invent extra conditions.
```

---

## 14. Evaluation Metrics

Useful metrics for LLM apps include:

- Exact match
- Semantic similarity
- Human rating
- LLM-as-judge rating
- Hallucination rate
- JSON validity
- Tool-call success rate
- Latency
- Cost per request
- User satisfaction

For classification tasks, we can also use traditional ML metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

---

## 15. Deployment

Deployment means making the AI app available to users.

Deployment includes:

- API server
- Frontend
- Environment variables
- Authentication
- Logging
- Monitoring
- Rate limiting
- Error handling
- CI/CD
- Secret management
- Cost tracking
- Safety filters

Calling an LLM locally is easy.

Deploying it reliably is the real engineering task.

---

## 16. Monitoring

After deployment, we need to monitor the system.

Important things to monitor:

- Token usage
- Cost
- Latency
- Errors
- Failed tool calls
- User feedback
- Hallucinations
- Unsafe outputs
- Retrieval quality
- Model version changes

Monitoring helps us improve the system over time.

---

## 17. Why Model Selection Matrix Matters

A model selection matrix helps compare models in a structured way.

Without a matrix, model choice becomes emotional or random.

A good matrix compares:

- Quality
- Cost
- Latency
- Privacy
- Ease of use
- Infrastructure complexity
- Best use case
- Main risk

The goal is not to choose the biggest model.

The goal is to choose the best model for the use case.

---

## 18. Model Selection Matrix Example

| Option | Quality | Cost | Latency | Privacy | Ease of Use | Infra Complexity | Best For | Main Risk |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Hosted frontier model | Very High | Medium to High | Medium | Medium | Very High | Low | Complex reasoning, production apps, fast prototyping | API cost and provider dependency |
| Hosted smaller model | Medium to High | Low to Medium | Low | Medium | Very High | Low | Classification, routing, simple summarization | May fail on complex reasoning |
| Open-weight small model | Medium | Low at scale | Low to Medium | High | Medium | Medium | Private/simple workloads, local experiments | Lower quality than frontier models |
| Open-weight large model | High | Medium to High infra cost | Medium to High | High | Low to Medium | High | Private enterprise workloads, custom deployment | GPU cost and ops complexity |
| Fine-tuned model | High for narrow task | Medium | Low to Medium | Depends | Medium | Medium | Repeated specialized tasks | Needs quality dataset |
| RAG + hosted model | High | Medium | Medium | Medium | High | Medium | Knowledge-grounded apps | Retrieval quality can limit answer quality |
| RAG + open-weight model | Medium to High | Medium | Medium | High | Medium | High | Private document QA | More infra and tuning required |

---

## 19. Simple Model Choice Examples

| Task | Suggested Model Type | Reason |
|---|---|---|
| Sentiment classification | Small hosted or small open-weight model | Simple task |
| Ticket routing | Small cheap model | Structured classification |
| Long document summarization | Long-context hosted model | Needs large context |
| Customer support FAQ | RAG + hosted model | Needs company knowledge |
| Private legal document QA | Open-weight or privacy-compliant hosted setup | Privacy matters |
| Coding assistant | Strong hosted model | Needs reasoning and code quality |
| Agentic workflow | Hosted model with strong tool calling | Needs reliable tool usage |

---

## 20. Practical Decision Framework

When selecting a model, ask:

```text
1. What is the task?
2. How difficult is the task?
3. How much quality is required?
4. How sensitive is the data?
5. What is the acceptable latency?
6. What is the budget?
7. Does the model need a long context window?
8. Does the model need tool/function calling?
9. Does the model need structured output?
10. Will this app need to scale?
11. Can we evaluate the model properly?
12. Can we monitor failures in production?
```

A good model choice balances:

```text
quality + cost + latency + privacy + reliability
```

---

## 21. Day 10 Summary

Today I learned:

- The GenAI lifecycle includes data, model choice, prompting, evaluation, deployment, monitoring, and improvement.
- Model selection should be based on task requirements, not hype.
- Hosted API models are easier to use and faster to deploy.
- Open-weight models offer more control and privacy but require more infrastructure work.
- A model selection matrix helps compare cost, latency, quality, privacy, and complexity.
- Evaluation is necessary before trusting an LLM in production.
- Deployment requires logging, monitoring, secrets, CI/CD, and cost tracking.
- The best model is not always the biggest model.
- The best model is the one that fits the product requirements.