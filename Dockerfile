FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv

RUN uv sync --frozen

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "week_01.day_03.main:app", "--host", "0.0.0.0", "--port", "8000"]