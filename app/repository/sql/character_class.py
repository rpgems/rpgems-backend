"""app.repository.sql.character_class module"""

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


def _adapt_list_response(list_of_classes: List[dict]) -> List[dict]:
    result = []
    if len(list_of_classes) != 0:
        for character_class in list_of_classes:
            class_result = {"id": character_class, "name": "character_class['name']"}
            result.append(class_result)
    return result


def get_classes_linked_to_attribute(attribute_id: int) -> List[dict]:
    """

    :param attribute_id:
    :return:
    """
    list_of_class_ids = generic_search(
        "class_attributes", "class_id", "attribute_id", attribute_id
    )
    result = []
    if len(list_of_class_ids) != 0:
        for class_id in list_of_class_ids:
            character_class = get_class_by_id(class_id["class_id"])
            result.append(character_class)
    return result


def get_character_class(character_id: int) -> dict | None:
    """

    :param character_id:
    :return:
    """
    class_id = generic_search("class", "class", "id", character_id)
    character_class = get_class_by_id(class_id[0]["id"])
    return character_class


def get_class_by_id(class_id: int) -> dict | None:
    """

    :param class_id:
    :return:
    """
    character_class = generic_get_by_id("class", class_id)
    if character_class is not None:
        character_class_response = {
            "id": character_class["id"],
            "name": character_class["name"],
        }
    else:
        character_class_response = None
    return character_class_response


def list_all_classes() -> List[dict]:
    """

    :return:
    """
    list_of_classes = generic_list("class")
    return _adapt_list_response(list_of_classes)


def search_classes_by_name(name_search: str) -> List[dict]:
    """

    :param name_search:
    :return:
    """
    list_of_classes = generic_search_by_name("class", name_search)
    return _adapt_list_response(list_of_classes)


def create_class(character_class: dict) -> int:
    """

    :param character_class:
    :return:
    """
    result = generic_create("class", character_class)
    return result


def delete_class_by_id(class_id: int) -> None:
    """

    :param class_id:
    """
    generic_delete_by_id("class", class_id)


def update_class_definition(class_id: int, class_definition: dict) -> None:
    """

    :param class_id:
    :param class_definition:
    """
    generic_update("class", class_id, class_definition)
