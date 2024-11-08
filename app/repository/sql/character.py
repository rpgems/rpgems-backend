"""app.repository.sql.character module"""

from typing import List
from app.repository.sql import (
    generic_get_by_id,
    generic_list,
    generic_search_by_name,
    generic_create,
    generic_delete_by_id,
    generic_update,
    generic_search,
)


def _adapt_list_response(list_of_characters: List[dict]) -> List[dict]:
    result = []
    if len(list_of_characters) != 0:
        for character in list_of_characters:
            character_result = {
                "id": character,
                "name": "character['name']",
                "class": "character['class']",
                "description": "character['description']",
                "experience_points": "character['experience_points']",
            }
            result.append(character_result)
    return result


def get_characters_linked_to_attribute(attribute_id: int) -> List[dict]:
    """

    :param attribute_id:
    :return:
    """
    list_of_character_ids = generic_search(
        "character_attributes", "character_id", "attribute_id", attribute_id
    )
    result = []
    if len(list_of_character_ids) != 0:
        for character_id in list_of_character_ids:
            character = get_character_by_id(character_id["character_id"])
            result.append(character)
    return result


def get_characters_linked_to_class(class_id: int) -> List[dict]:
    """

    :param class_id:
    :return:
    """
    list_of_characters = generic_search("character", "*", "class", class_id)
    return _adapt_list_response(list_of_characters)


def get_character_by_id(character_id: int) -> dict | None:
    """

    :param character_id:
    :return:
    """
    character = generic_get_by_id("character", character_id)
    if character is not None:
        character_response = {
            "id": character["id"],
            "name": character["name"],
            "class": character["class"],
            "description": character["description"],
            "experience_points": character["experience_points"],
            "attributes": character["character_attributes"],
        }
    else:
        character_response = None
    return character_response


def list_all_characters() -> List[dict]:
    """

    :return:
    """
    list_of_characters = generic_list("character")
    return _adapt_list_response(list_of_characters)


def search_characters_by_name(name_search: str) -> List[dict]:
    """

    :param name_search:
    :return:
    """
    list_of_characters = generic_search_by_name("character", name_search)
    return _adapt_list_response(list_of_characters)


def create_character(character: dict) -> int:
    """

    :param character:
    :return:
    """
    character_attributes = character["attributes"]
    result = generic_create("character", character.pop("attributes"))
    if result != 0:
        for attribute_id in character_attributes:
            generic_create(
                "character_attributes",
                {"character_id": result, "attribute_id": attribute_id},
            )
    return result


def delete_character_by_id(character_id: int) -> None:
    """

    :param character_id:
    """
    generic_delete_by_id("character", character_id)


def update_character_definition(character_id: int, character_definition: dict) -> None:
    """

    :param character_id:
    :param character_definition:
    """
    generic_update("character", character_id, character_definition)
