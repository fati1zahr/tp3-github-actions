import pytest

from app.web import create_app 

@pytest.fixture
def client():
 app = create_app()
 app.config["TESTING"] = True
 return app.test_client()

def test_moderate_autoriser(client):
    response = client.post("/moderate", json={"message": "Hello, this is a test."})
    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}


def test_moderate_bloquer(client):
    response = client.post("/moderate", json={"message": "This is as Spam message"})
    assert response.status_code == 200
    assert response.get_json()== {"decision": "bloquer" }

def test_moderate_invalid(client):
    response = client.post("/moderate", json={"message":42})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}

def test_moderate_not_json(client):
    response = client.post("/moderate", data="ceci n'est pas du json")
    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}