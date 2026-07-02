# tests/test_routes.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_conversation_api():
    payload = {
        "description": "Sustainability in smart cities",
        "interests": ["green energy", "public transport"]
    }

    response = client.post("/generate-conversation", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "topics" in data
    assert "suggestions" in data
    assert isinstance(data["topics"], list)
    assert isinstance(data["suggestions"], list)


def test_fact_check_api():
    response = client.post(
        "/fact-check",
        json={"query": "solar energy"}
    )

    assert response.status_code == 200

    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)


def test_analyze_event_api():
    response = client.post(
        "/analyze-event",
        json={"description": "AI in healthcare and medical diagnostics"}
    )

    assert response.status_code == 200

    data = response.json()
    assert "topics" in data
    assert isinstance(data["topics"], list)


def test_invalid_request_returns_422():
    # Missing required fields
    response = client.post("/generate-conversation", json={})

    assert response.status_code == 422