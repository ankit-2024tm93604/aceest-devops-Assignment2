import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add_client():
    client = app.test_client()
    
    response = client.post("/clients", json={
        "name": "TestUser",
        "age": 30,
        "weight": 80,
        "program": "Fat Loss"
    })
    
    assert response.status_code == 200

def test_get_client():
    client = app.test_client()
    response = client.get("/clients/TestUser")
    assert response.status_code in [200, 404]

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200