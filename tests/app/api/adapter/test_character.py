"""
tests.app.api.adapter.test_character
"""
import pytest
from fastapi import HTTPException, status

from app.api.adapter.character import adapt_get_character_by_id, adapt_search_characters_by_name, \
    adapt_create_character


def test_get_character_by_id_with_invalid_id():
    invalid_id = 'invalid_id'
    with pytest.raises(HTTPException) as exc_info:
        adapt_get_character_by_id(invalid_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert exc_info.value.detail == "Character id should be a number"


def test_search_characters_by_name_with_empty_name():
    name = ""
    with pytest.raises(HTTPException) as exc_info:
        adapt_search_characters_by_name(name)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert exc_info.value.detail == "Name should be a non-empty string"


def test_create_character_with_only_character_name():
    character_definition = {"name": "character_name"}
    with pytest.raises(HTTPException) as exc_info:
        adapt_create_character(character_definition)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert exc_info.value.detail == ('Missing required fields: ["character_class",'
                                         ' "description", "experience_points",'
                                         ' "character_attributes"]')
