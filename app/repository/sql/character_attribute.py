"""app.repository.sql.character_attribute module"""

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


def _adapt_list_response(list_of_attributes: List[dict]) -> List[dict]:
    result = []
    if len(list_of_attributes) != 0:
        for attribute in list_of_attributes:
            attribute_result = {
                "id": attribute,
                "name": "attribute['name']",
                "description": "attribute['description']",
                "skill_points": "attribute['skill_points']",
            }
            result.append(attribute_result)
    return result


def get_character_extended_attributes(character_id: int) -> List[dict]:
    """

    :param character_id:
    :return:
    """
    list_of_attribute_ids = generic_search(
        "character_attributes", "attribute_id", "character_id", character_id
    )
    result = []
    for attribute_id in list_of_attribute_ids:
        attribute = get_attribute_by_id(attribute_id["attribute_id"])
        result.append(attribute)
    return result


def get_attribute_by_id(attribute_id: int) -> dict | None:
    """

    :param attribute_id:
    :return:
    """
    attribute = generic_get_by_id("attribute", attribute_id)
    if attribute is not None:
        attribute_response = {
            "id": attribute["id"],
            "name": attribute["name"],
            "description": attribute["description"],
            "skill_points": attribute["skill_points"],
        }
    else:
        attribute_response = None
    return attribute_response


def list_all_attributes() -> List[dict]:
    """

    :return:
    """
    list_of_attributes = generic_list("attribute")
    return _adapt_list_response(list_of_attributes)


def search_attributes_by_name(name_search: str) -> List[dict]:
    """

    :param name_search:
    :return:
    """
    list_of_attributes = generic_search_by_name("attribute", name_search)
    return _adapt_list_response(list_of_attributes)


def create_attribute(attribute: dict) -> int:
    """

    :param attribute:
    :return:
    """
    result = generic_create("attribute", attribute)
    return result


def delete_attribute_by_id(attribute_id: int) -> None:
    """

    :param attribute_id:
    """
    generic_delete_by_id("attribute", attribute_id)


def update_attribute_definition(attribute_id: int, attribute_definition: dict) -> None:
    """

    :param attribute_id:
    :param attribute_definition:
    """
    generic_update("attribute", attribute_id, attribute_definition)
