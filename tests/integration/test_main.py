import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "H=0 Dominion Etched: Fluid Gnosis Active"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "Operational"
    assert response.json()["replicas"] == 400
