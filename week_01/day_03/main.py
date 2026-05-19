import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, Field

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Engineer Labs API")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


app = FastAPI(title=APP_NAME)


class HealthResponse(BaseModel):
    status: str
    environment: str


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)


class ChatResponse(BaseModel):
    reply: str


class FeedbackRequest(BaseModel):
    message_id: str = Field(..., min_length=1)
    rating: int = Field(..., ge=1, le=5)
    comment: str | None = None


class FeedbackResponse(BaseModel):
    status: str
    message: str


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", environment=ENVIRONMENT)


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    reply = f"You said: {request.message}"
    return ChatResponse(reply=reply)


@app.post("/feedback", response_model=FeedbackResponse)
def feedback(request: FeedbackRequest) -> FeedbackResponse:
    return FeedbackResponse(
        status="received",
        message=f"Feedback received for message_id: {request.message_id}",
    )
