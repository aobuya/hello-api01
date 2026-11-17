from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_greeting():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from API"}


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.text == "OK"


def test_unknown_route_is_404():
    response = client.get("/does-not-exist")
    assert response.status_code == 404

