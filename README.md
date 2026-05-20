# AI Engineer Labs

This repository contains my hands-on labs, notes, and mini-projects while following my Agentic AI Engineer roadmap.

## Goal

Become job-ready for AI Engineer, GenAI Engineer, Applied AI Engineer, and Agentic AI Engineer roles by building production-grade AI applications.

## Weekly Roadmap

| Week | Focus | Outcome |
|---|---|---|
| Week 1 | Production Python, Git, APIs, and AI engineering setup | Clean Python repo, FastAPI basics, tests, Docker, CI |
| Week 2 | ML, deep learning, transformers, and LLM foundations | ML notebooks, PyTorch basics, LLM API wrapper |
| Week 3 | Embeddings, semantic search, and RAG fundamentals | Local RAG prototype with citations |
| Week 4 | Advanced RAG and Project 1 sprint | Enterprise RAG Copilot MVP |
| Week 5 | Agents, tool calling, and LangGraph fundamentals | Stateful LangGraph agent |
| Week 6 | Multi-agent research planner | Project 2 MVP |
| Week 7 | Evals, observability, safety, and reliability | Shared eval and tracing setup |
| Week 8 | Agentic PR reviewer | Project 3 MVP |
| Week 9 | Cloud, CI/CD, monitoring, production hardening | Portfolio-grade deployed projects |
| Week 10 | Resume, interviews, and applications | Job search package |

## Daily Rule

Every study day must produce at least one of the following:

- Code
- Notes
- Tests
- Documentation
- Evaluation artifact
- GitHub commit

## Running the FastAPI app with Docker

This project includes a Dockerized FastAPI app.

### Build the Docker image manually

```bash
docker build -t ai-engineer-fastapi .

## Production environment variables

This project uses environment variables for configuration.

For local development, create a `.env` file in the project root:

```bash
cp .env.example .env