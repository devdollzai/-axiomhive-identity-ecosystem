import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_api_endpoints():
    response = client.get("/api/metrics")
    assert response.status_code == 200
