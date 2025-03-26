from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_update_item():
    response = client.put("/items/1", json={"name": "test", "price": 10.5})
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 1,
        "item": {"name": "test", "price": 10.5, "description": None, "tax": None},
    }


def test_update_item_with_query():
    response = client.put("/items/1?q=test", json={"name": "test", "price": 10.5})
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 1,
        "q": "test",
        "item": {"name": "test", "price": 10.5, "description": None, "tax": None},
    }


def test_update_item_invalid_id():
    response = client.put("/items/1001", json={"name": "test", "price": 10.5})
    assert response.status_code == 422


def test_update_item_negative_id():
    response = client.put("/items/-1", json={"name": "test", "price": 10.5})
    assert response.status_code == 422


def test_update_item_without_body():
    response = client.put("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}
