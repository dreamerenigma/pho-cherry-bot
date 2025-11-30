import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json().get("message", "")

def test_get_menu():
    response = client.get("/menu")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    
    if data:
        assert "name" in data[0] and "price" in data[0]
