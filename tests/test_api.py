from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_empty_question():
    response = client.post("/ask", json={"question": ""})
    assert response.status_code == 200
    assert response.json()["answer"] == "Please enter a question."


def test_invalid_request():
    response = client.post("/ask", json={})
    assert response.status_code == 422


def test_accommodation_fallback():
    response = client.post(
        "/ask",
        json={"question": "Does Zaio provide free accommodation to students?"}
    )
    assert response.status_code == 200
    assert response.json()["answer"] == (
        "I don't know. The handbook does not provide this information."
    )


def test_attendance_fallback():
    response = client.post(
        "/ask",
        json={"question": "What is the attendance requirement?"}
    )
    assert response.status_code == 200
    assert response.json()["answer"] == (
        "I don't know. The handbook does not provide this information."
    )