from fastapi.testclient import TestClient

from week_01.day_03 import main

client = TestClient(main.app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_endpoint() -> None:
    response = client.post(
        "/chat",
        json={"message": "Hello"},
    )

    assert response.status_code == 200
    assert "reply" in response.json()


def test_chat_endpoint_with_mocked_llm_response(monkeypatch) -> None:
    def fake_llm_response(message: str) -> str:
        return f"Mocked response for: {message}"

    monkeypatch.setattr(main, "get_llm_response", fake_llm_response)

    response = client.post(
        "/chat",
        json={"message": "What is FastAPI?"},
    )

    assert response.status_code == 200
    assert response.json() == {"reply": "Mocked response for: What is FastAPI?"}
