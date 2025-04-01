from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_items_with_valid_headers():
    """Test read_items endpoint with valid headers."""
    response = client.get(
        "/items/",
        headers={
            "X-Token": "fake-super-secret-token",
            "X-Key": "fake-super-secret-key",
        },
    )
    assert response.status_code == 200
    assert response.json() == [{"item": "Foo"}, {"item": "Bar"}]


def test_read_items_with_invalid_token():
    """Test read_items endpoint with invalid token."""
    response = client.get(
        "/items/",
        headers={"X-Token": "invalid-token", "X-Key": "fake-super-secret-key"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}


def test_read_items_with_invalid_key():
    """Test read_items endpoint with invalid key."""
    response = client.get(
        "/items/",
        headers={"X-Key": "invalid-key"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Key header invalid"}


def test_read_items_without_headers():
    """Test read_items endpoint without headers."""
    response = client.get("/items/")
    assert response.status_code == 422
    assert "detail" in response.json()
