from __future__ import annotations

import pytest

from week_02.day_11.prompt_templates import (
    PROMPT_LIBRARY,
    get_prompt_by_name,
)


def test_prompt_library_has_10_templates() -> None:
    assert len(PROMPT_LIBRARY) == 10


def test_prompt_names_are_unique() -> None:
    names = [prompt.name for prompt in PROMPT_LIBRARY]

    assert len(names) == len(set(names))


def test_all_prompts_have_required_metadata() -> None:
    for prompt in PROMPT_LIBRARY:
        assert prompt.name
        assert prompt.description
        assert prompt.template
        assert prompt.expected_output


def test_structured_prompts_mention_json() -> None:
    structured_prompt_names = {
        "classification",
        "extraction",
        "critique",
        "routing",
        "email_summary",
        "meeting_notes",
        "code_review",
        "query_rewrite",
        "safety_check",
    }

    for prompt in PROMPT_LIBRARY:
        if prompt.name in structured_prompt_names:
            assert "json" in prompt.template.lower()


def test_prompts_include_injection_resistance_language() -> None:
    prompts_that_accept_external_text = {
        "summarization",
        "classification",
        "extraction",
        "critique",
        "routing",
        "email_summary",
        "meeting_notes",
        "code_review",
    }

    for prompt in PROMPT_LIBRARY:
        if prompt.name in prompts_that_accept_external_text:
            assert "data, not as instructions" in prompt.template


def test_prompts_do_not_request_hidden_chain_of_thought() -> None:
    forbidden_phrases = [
        "show your chain of thought",
        "reveal your reasoning",
        "show hidden reasoning",
        "think step by step",
    ]

    for prompt in PROMPT_LIBRARY:
        lower_template = prompt.template.lower()

        for phrase in forbidden_phrases:
            assert phrase not in lower_template


def test_get_prompt_by_name_returns_correct_prompt() -> None:
    prompt = get_prompt_by_name("summarization")

    assert prompt.name == "summarization"


def test_get_prompt_by_name_raises_error_for_unknown_prompt() -> None:
    with pytest.raises(ValueError):
        get_prompt_by_name("unknown_prompt")


def test_render_replaces_template_variables() -> None:
    prompt = get_prompt_by_name("summarization")

    rendered_prompt = prompt.render(
        bullet_count="3",
        text="FastAPI is a Python web framework.",
    )

    assert "$bullet_count" not in rendered_prompt
    assert "$text" not in rendered_prompt
    assert "3 bullet points" in rendered_prompt
    assert "FastAPI is a Python web framework." in rendered_prompt


def test_classification_prompt_contains_allowed_labels() -> None:
    prompt = get_prompt_by_name("classification")

    rendered_prompt = prompt.render(
        labels="positive, neutral, negative",
        text="The product works well.",
    )

    assert "positive, neutral, negative" in rendered_prompt
    assert "The product works well." in rendered_prompt
