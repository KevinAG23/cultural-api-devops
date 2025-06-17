import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import pytest
from app import app  


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_cultural_greeting_status_code(client):
    response = client.get('/cultural-greeting')
    assert response.status_code == 200

def test_cultural_greeting_content(client):
    response = client.get('/cultural-greeting')
    data = response.get_json()
    assert "greetings" in data
    greetings = data["greetings"]

    # Validar algunos países clave
    assert "Ecuador" in greetings
    assert greetings["Ecuador"] == "¡Hola!"

    assert "India" in greetings
    assert greetings["India"] == "नमस्ते"
