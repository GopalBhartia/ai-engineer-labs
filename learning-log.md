## Week 1 Reflection

### What I built

In Week 1, I set up the foundation for my AI Engineer learning project. I created the `ai-engineer-labs` GitHub repository, configured a Python development environment with `uv`, and organized the project using a weekly/day-wise folder structure.

I practiced Python type hints and created Pydantic models for AI app data structures such as user queries, retrieved chunks, agent state, tool calls, and evaluation results. I also added code quality tools like `ruff` and `pre-commit`.

I built a basic FastAPI app with endpoints, added tests for the API, Dockerized the FastAPI app, and deployed it to Render.

### What broke or confused me

Some parts that were confusing or required debugging:

- Understanding how Python virtual environments and `uv` work.
- Understanding type hints such as `Protocol`, `TypedDict`, `Optional`, and `Literal`.
- Understanding Pydantic concepts such as `default_factory`.
- Fixing FastAPI `422 Validation Error` issues when the request body did not match the expected schema.
- Understanding how the FastAPI app path maps to the Uvicorn import path, such as `week_01.day_03.main:app`.
- Understanding Docker concepts such as image, container, port mapping, `Dockerfile`, and `.dockerignore`.
- Understanding why the deployed Render root URL showed `{"detail":"Not Found"}` before adding or checking the correct route.
- Waiting for Render auto-deploy and learning that deploys may take some time after a GitHub push.

### What I fixed

I fixed the project structure to consistently use underscore-based folders like `week_01/day_03/`.

I fixed FastAPI request issues by making sure the request body matched the expected Pydantic model.

I added tests for the FastAPI app and verified them using `pytest`.

I created a working `Dockerfile`, `.dockerignore`, and `docker-compose.yml` so the API can run locally inside Docker.

I deployed the API to Render and learned how to configure the build command, start command, Python version, and production environment variables.

### What I learned

I learned how to structure a Python backend project, use type safety, validate data with Pydantic, build APIs with FastAPI, test endpoints, containerize an app with Docker, and deploy a live API.

I also learned that production apps need clear documentation, environment variable management, and consistent project structure.

### What I want to improve next week

In Week 2, I want to get more comfortable with building real AI app features. I want to understand how LLM APIs, prompts, retrieval, embeddings, and vector databases fit together in practical applications.

I also want to continue improving my debugging skills and write cleaner, better-tested code.