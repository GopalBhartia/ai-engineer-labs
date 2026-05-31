# Day 10: Model Selection Matrix

## Goal

The goal of this matrix is to compare different model options before choosing one for a GenAI application.

A good AI engineer should not choose a model randomly.

Model choice should depend on:

- Quality
- Cost
- Latency
- Privacy
- Context window
- Tool support
- Deployment complexity
- Reliability
- Fine-tuning needs
- Production constraints

---

## Example Use Case

Use case:

```text
Build a customer-support assistant that answers user questions from company documents.
```

The assistant should:

- Answer accurately
- Avoid hallucinations
- Use retrieved company documents
- Respond quickly
- Keep cost reasonable
- Protect private company data
- Escalate uncertain cases to a human

---

## Model Selection Matrix

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

## Scoring Criteria

| Criterion | Meaning |
|---|---|
| Quality | How accurate and useful the model output is |
| Cost | How expensive the model is per request or at scale |
| Latency | How fast the model responds |
| Privacy | How much control we have over user/company data |
| Ease of Use | How easy it is to integrate and maintain |
| Infra Complexity | How much engineering work is needed to run it |
| Best For | The most suitable use case |
| Main Risk | The biggest downside |

---

## Practical Recommendation

For an early-stage AI app or portfolio project, I would usually start with:

```text
RAG + hosted API model
```

Reason:

- Fast to build
- Good answer quality
- No GPU infrastructure required
- Easy to deploy
- Easy to iterate
- Good for learning production AI patterns

After the app grows, I can optimize by:

- Using smaller models for simple tasks
- Caching repeated responses
- Using cheaper models for classification/routing
- Using stronger models only for complex reasoning
- Testing open-weight models for privacy or cost control
- Fine-tuning only when prompting/RAG is not enough

---

## Example Model Choice by Task

| Task | Suggested Model Type | Reason |
|---|---|---|
| Sentiment classification | Small hosted or small open-weight model | Simple task, does not need strongest model |
| Long document summarization | Long-context hosted model | Needs large context and good summarization |
| Private legal document QA | Open-weight model or privacy-compliant hosted setup | Privacy matters |
| Coding assistant | Strong hosted model | Requires reasoning and code quality |
| Customer support FAQ | RAG + hosted smaller/medium model | Needs company knowledge and reasonable cost |
| Medical diagnosis assistant | Strong model with strict safety, evals, and human review | High-risk domain |
| Ticket routing | Small cheap model | Structured classification task |
| Agentic workflow with tools | Hosted model with strong tool/function calling | Needs reliability and tool use |

---

## Final Decision Framework

When selecting a model, ask:

```text
1. How difficult is the task?
2. How much quality do users need?
3. How sensitive is the data?
4. What is the acceptable latency?
5. What is the budget?
6. Does the model need tools/function calling?
7. Does the model need a long context window?
8. Will the app need to scale?
9. Can we evaluate the model reliably?
10. Can we monitor failures in production?
```

A good model choice is not the most powerful model.

A good model choice is the model that best balances:

```text
quality + cost + latency + privacy + reliability
```