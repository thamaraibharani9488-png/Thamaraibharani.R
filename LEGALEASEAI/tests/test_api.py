from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["name"] == "LegalEase"


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_generate():

    payload = {
        "document_type": "Freelance Work Contract",

        "parties": (
            "Jane Doe (Provider), "
            "ABC Corp (Client)"
        ),

        "terms": (
            "Payment within 30 days; "
            "Confidentiality applies"
        ),

        "effective_date": "2026-09-29",
    }

    response = client.post(
        "/generate",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert (
        body["document_type"]
        == payload["document_type"]
    )

    assert len(
        body["content"]
    ) > 50