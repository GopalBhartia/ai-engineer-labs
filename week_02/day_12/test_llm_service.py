import pytest

from week_02.day_12.llm_service import (
    LLMResponse,
    LLMService,
    TokenCostLog,
)


class FakeModelClient:
    """Fake model client used for testing."""

    def generate(self, prompt: str) -> str:
        """Return predictable output for tests."""
        return f"Fake output for: {prompt}"


def test_generate_reply_returns_structured_response() -> None:
    model_client = FakeModelClient()
    service = LLMService(
        model_client=model_client,
        model_name="fake-test-model",
    )

    response = service.generate_reply("Explain token logging.")

    assert isinstance(response, LLMResponse)
    assert response.prompt == "Explain token logging."
    assert response.output == "Fake output for: Explain token logging."
    assert response.model_name == "fake-test-model"


def test_generate_reply_strips_extra_whitespace() -> None:
    model_client = FakeModelClient()
    service = LLMService(model_client=model_client)

    response = service.generate_reply("   Hello model   ")

    assert response.prompt == "Hello model"
    assert response.output == "Fake output for: Hello model"


def test_generate_reply_rejects_empty_prompt() -> None:
    model_client = FakeModelClient()
    service = LLMService(model_client=model_client)

    with pytest.raises(ValueError, match="Prompt cannot be empty"):
        service.generate_reply("   ")


def test_generate_reply_includes_usage_placeholder() -> None:
    model_client = FakeModelClient()
    service = LLMService(model_client=model_client)

    response = service.generate_reply("Count these tokens")

    assert isinstance(response.usage, TokenCostLog)
    assert response.usage.prompt_tokens > 0
    assert response.usage.completion_tokens > 0
    assert response.usage.total_tokens > 0
    assert response.usage.estimated_cost_usd == 0.0
