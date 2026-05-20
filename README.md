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

### Build the Docker image manually

```bash
docker build -t ai-engineer-fastapi .
```

### Run the container manually

```bash
docker run --name ai-engineer-api -p 8000:8000 ai-engineer-fastapi
```

The API will be available at:

```text
http://localhost:8000
```

Swagger UI will be available at:

```text
http://localhost:8000/docs
```

### Run with Docker Compose

```bash
docker compose up --build
```

### Stop Docker Compose

```bash
docker compose down
```

## Production environment variables

This project uses environment variables for configuration.

For local development, create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then fill in the required values in `.env`.

Example variables:

```env
ENVIRONMENT=development
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=postgresql://app_user:app_password@localhost:5432/app_db
```

Never commit real secrets such as API keys, database passwords, or tokens.

For Render deployment:

1. Open the Render dashboard.
2. Select the deployed web service.
3. Go to **Environment**.
4. Add production values for required variables.
5. Redeploy the service if needed.

Example production variables:

```env
ENVIRONMENT=production
OPENAI_API_KEY=<real-production-key>
DATABASE_URL=<production-database-url>
```

## Live API

The FastAPI app is deployed on Render.

Live API:

```text
https://ai-engineer-fastapi.onrender.com/
```

Swagger UI:

```text
https://ai-engineer-fastapi.onrender.com/docs
```

## Deployment notes

The app is deployed using Render as a Python Web Service.

Render build command:

```bash
pip install uv && uv sync --frozen
```

Render start command:

```bash
uv run uvicorn week_01.day_03.main:app --host 0.0.0.0 --port $PORT
```

The `$PORT` value is provided by Render in production.