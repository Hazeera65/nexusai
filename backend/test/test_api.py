
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_document_preview_success():
    content = "Refunds are allowed within 30 days."

    response = client.post(
        "/api/v1/documents/preview",
        json={
            "title": "Refund Policy",
            "content": content,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "title": "Refund Policy",
        "character_count": len(content),
        "status": "validated",
    }



def test_document_preview_rejects_empty_title():
    response = client.post(
        "/api/v1/documents/preview",
        json={
            "title": "",
            "content": "Sample document",
        },
    )

    assert response.status_code == 422


def test_document_preview_rejects_missing_content():
    response = client.post(
        "/api/v1/documents/preview",
        json={"title": "Refund Policy"},
    )

    assert response.status_code == 422
