from http import HTTPStatus

from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health_check")

    assert response.status_code == HTTPStatus.OK
