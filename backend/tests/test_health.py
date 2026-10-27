"""Example unit test. Each test maps to an acceptance criterion of a spec.

Spec: docs/specs/001-health-check.md
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_200_and_ok_status():
    # AC1: GET /health answers 200
    # AC2: the body is {"status": "ok"}
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_rejects_non_get_methods():
    # AC3: only GET is allowed
    response = client.post("/health")

    assert response.status_code == 405
