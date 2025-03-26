from fastapi.testclient import TestClient
from app.main import Param, app

client = TestClient(app)


def test_valid_no_param():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_valid_simple_param():
    response = client.get("/ABC")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello ABC"}


def test_valid_param_A():
    response = client.get("/param/a")
    assert response.status_code == 200, response.json()
    assert response.json() == {"message": f"Hello {Param.A.name}"}
