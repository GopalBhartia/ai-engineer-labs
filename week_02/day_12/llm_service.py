from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class ModelClient(Protocol):
    """Protocol for any model client that can generate text.

    This allows us to use:
    - a real OpenAI-backed client in production
    - a fake/mock client in unit tests
    - another provider later without changing LLMService
    """

    def generate(self, prompt: str) -> str:
        """Generate a model response from a prompt."""
        ...


@dataclass
class TokenCostLog:
    """Stores placeholder usage and cost information for an LLM call.

    We are not calculating real usage yet. This class gives us a clean place
    to store those values later when we connect real token counting.
    """

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    estimated_cost_usd: float = 0.0


@dataclass
class LLMResponse:
    """Represents a clean response returned by our LLM service."""

    prompt: str
    output: str
    model_name: str
    usage: TokenCostLog


class SimpleMockModelClient:
    """A simple fake model client for local development and tests.

    This does not call a real LLM. It returns a predictable response.
    """

    def generate(self, prompt: str) -> str:
        """Return a predictable response for a given prompt."""
        return f"Mocked LLM response for: {prompt}"


class LLMService:
    """Service class that wraps model calls behind a clean interface."""

    def __init__(
        self,
        model_client: ModelClient,
        model_name: str = "mock-model",
    ) -> None:
        self.model_client = model_client
        self.model_name = model_name

    def generate_reply(self, prompt: str) -> LLMResponse:
        """Generate a reply from the model and return structured metadata."""

        cleaned_prompt = prompt.strip()

        if not cleaned_prompt:
            raise ValueError("Prompt cannot be empty.")

        output = self.model_client.generate(cleaned_prompt)

        usage = self._build_usage_placeholder(
            prompt=cleaned_prompt,
            output=output,
        )

        return LLMResponse(
            prompt=cleaned_prompt,
            output=output,
            model_name=self.model_name,
            usage=usage,
        )

    def _build_usage_placeholder(
        self,
        prompt: str,
        output: str,
    ) -> TokenCostLog:
        """Create placeholder token and cost logging data.

        This is intentionally approximate for now. Later, we can replace this
        with real token usage returned by an API provider or tokenizer.
        """

        estimated_prompt_tokens = len(prompt.split())
        estimated_completion_tokens = len(output.split())
        estimated_total_tokens = estimated_prompt_tokens + estimated_completion_tokens

        return TokenCostLog(
            prompt_tokens=estimated_prompt_tokens,
            completion_tokens=estimated_completion_tokens,
            total_tokens=estimated_total_tokens,
            estimated_cost_usd=0.0,
        )


def main() -> None:
    """Run a small local demo."""

    model_client = SimpleMockModelClient()
    llm_service = LLMService(
        model_client=model_client,
        model_name="mock-model",
    )

    response = llm_service.generate_reply("Explain why service classes are useful.")

    print("Prompt:", response.prompt)
    print("Output:", response.output)
    print("Model:", response.model_name)
    print("Usage:", response.usage)


if __name__ == "__main__":
    main()
