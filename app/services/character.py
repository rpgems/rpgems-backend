"""app.services.character module"""
from typing import List

from fastapi import HTTPException, status

from app.domain.character import Character
from app.repository.sql.character import (get_character_by_id, list_all_characters, search_characters_by_name,
                                          create_character, delete_character_by_id, update_character_definition)


def service_get_character_by_id(character_id: int) -> Character:
    """

    :param character_id:
    :return:
    """
    if isinstance(character_id, int):
        character_data: dict = get_character_by_id(character_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Character id should be a number")
    if character_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
    character: Character = Character()
    character.id = character_id
    character.name = character_data["name"]
    character.character_class = character_data["class"]
    character.description = character_data["description"]
    character.experience_points = character_data["experience_points"]
    character.attributes = character_data["attributes"]
    return character


def service_list_characters() -> List[Character]:
    """

    :return:
    """
    character_list_data: List[dict] = list_all_characters()
    if len(character_list_data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No characters found")
    character_list: List[Character] = []
    for character_data in character_list_data:
        character: Character = Character()
        character.id = character_data["id"]
        character.name = character_data["name"]
        character.character_class = character_data["class"]
        character.description = character_data["description"]
        character.experience_points = character_data["experience_points"]
        character.attributes = character_data["attributes"]
        character_list.append(character)
    return character_list


def service_search_characters_by_name(name: str) -> List[Character]:
    """

    :param name:
    :return:
    """
    if len(name) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name should be a non-empty string")
    character_list_data: List[dict] = search_characters_by_name(name)
    if len(character_list_data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No characters found")
    character_list: List[Character] = []
    for character_data in character_list_data:
        character: Character = Character()
        character.id = character_data["id"]
        character.name = character_data["name"]
        character.character_class = character_data["class"]
        character.description = character_data["description"]
        character.experience_points = character_data["experience_points"]
        character.attributes = character_data["attributes"]
        character_list.append(character)
    return character_list


def service_create_character(character_data: dict) -> int:
    """

    :param character_data:
    :return:
    """
    keys = ["name", "character_class", "description", "experience_points", "character_attributes"]
    if all(key in keys for key in character_data.keys()):
        character_id: int = create_character(character_data)
    else:
        missing_fields = list(set(keys) - set(character_data.keys()))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Missing required fields: {missing_fields}")
    return character_id


def service_delete_character_by_id(character_id: int) -> None:
    """

    :param character_id:
    """
    if isinstance(character_id, int):
        character_data: dict = get_character_by_id(character_id)
        if character_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
        delete_character_by_id(character_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Character id should be a number")


def service_update_character_definition(character_id: int, definition: dict) -> dict:
    """

    :param character_id:
    :param definition:
    :return:
    """
    keys = ["name", "character_class", "description", "experience_points", "character_attributes"]
    if not isinstance(character_id, int):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Character id should be a number")
    if not definition.keys() in keys:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"malformed keys: {definition.keys()}")
    character_data: dict = get_character_by_id(character_id)
    if character_data is None:
        character_id: int = create_character(definition)
        result = {
            "content": {"message": "Character created"},
            "status": status.HTTP_201_CREATED,
            "headers": {"Content-Type": "application/json", "Location": f"/character/{character_id}"}
        }
    else:
        for key, value in definition.items():
            character_data[key] = value
        update_character_definition(character_id, character_data)
        result = {
            "content": {"message": "Character updated"},
            "status": status.HTTP_200_OK,
            "headers": {"Content-Type": "application/json"}
        }
    return result
