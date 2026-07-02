from tests.conftest import client


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Networking Assistant API!"
    }


def test_analyze_event():
    payload = {
        "description": "An AI networking conference focused on healthcare innovation."
    }

    response = client.post("/analyze-event", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "topics" in data
    assert isinstance(data["topics"], list)


def test_generate_conversation():
    payload = {
        "description": "An AI networking conference.",
        "interests": ["AI", "Machine Learning"]
    }

    response = client.post("/generate-conversation", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "topics" in data
    assert "suggestions" in data
    assert isinstance(data["topics"], list)
    assert isinstance(data["suggestions"], list)


def test_fact_check():
    payload = {
        "query": "Artificial intelligence"
    }

    response = client.post("/fact-check", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)