"""
tests.app.api.routes.test_character
"""
from fastapi.testclient import TestClient
from fastapi import status
from app.main import app


client = TestClient(app)

def test_get_character_by_id_with_character_not_found():
    response = client.get('/api/v1/character/0')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Character not found"}
