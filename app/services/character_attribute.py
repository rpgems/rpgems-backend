"""app.services.character_attribute module"""
from typing import List

from fastapi import HTTPException
from starlette import status

from app.domain.character_attribute import Attribute
from app.repository.sql.character_attribute import (get_attribute_by_id, list_all_attributes, search_attributes_by_name,
                                                    create_attribute, delete_attribute_by_id,
                                                    update_attribute_definition)


def service_get_attribute_by_id(attribute_id: int) -> Attribute:
    """

    :param attribute_id:
    :return:
    """
    if isinstance(attribute_id, int):
        character_response: dict = get_attribute_by_id(attribute_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="attribute_id should be a number")
    if character_response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="attribute not found")
    attribute = Attribute()
    attribute.id = attribute_id
    attribute.name = character_response['name']
    attribute.description = character_response['description']
    attribute.skill_points = character_response['skill_points']
    return attribute


def service_list_attributes() -> List[Attribute]:
    """

    :return:
    """
    attribute_list_data: List[dict] = list_all_attributes()
    if len(attribute_list_data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attributes found")
    attribute_list: List[Attribute] = []
    for attribute_data in attribute_list_data:
        attribute: Attribute = Attribute()
        attribute.id = attribute_data["id"]
        attribute.name = attribute_data["name"]
        attribute.description = attribute_data["description"]
        attribute.skill_points = attribute_data["skill_points"]
        attribute_list.append(attribute)
    return attribute_list


def service_search_attributes_by_name(name: str) -> List[Attribute]:
    """

    :param name:
    :return:
    """
    if len(name) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name should be a non-empty string")
    attribute_list_data: List[dict] = search_attributes_by_name(name)
    if len(attribute_list_data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attributes found")
    attribute_list: List[Attribute] = []
    for attribute_data in attribute_list_data:
        attribute: Attribute = Attribute()
        attribute.id = attribute_data["id"]
        attribute.name = attribute_data["name"]
        attribute.description = attribute_data["description"]
        attribute.skill_points = attribute_data["skill_points"]
        attribute_list.append(attribute)
    return attribute_list


def service_create_attribute(attribute_data: dict) -> int:
    """

    :param attribute_data:
    :return:
    """
    keys = ["name", "description", "skill_points"]
    if all(key in keys for key in attribute_data.keys()):
        attribute_id: int = create_attribute(attribute_data)
    else:
        missing_fields = list(set(keys) - set(attribute_data.keys()))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Missing required fields: {missing_fields}")
    return attribute_id


def service_delete_attribute_by_id(attribute_id: int) -> None:
    """

    :param attribute_id:
    """
    if isinstance(attribute_id, int):
        attribute_data: dict = get_attribute_by_id(attribute_id)
        if attribute_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attribute not found")
        delete_attribute_by_id(attribute_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Attribute id should be a number")


def service_update_attribute_definition(attribute_id: int, definition: dict) -> dict:
    """

    :param attribute_id:
    :param definition:
    :return:
    """
    keys = ["name", "description", "skill_points"]
    if not isinstance(attribute_id, int):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Attribute id should be a number")
    if not definition.keys() in keys:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"malformed keys: {definition.keys()}")
    attribute_data: dict = get_attribute_by_id(attribute_id)
    if attribute_data is None:
        attribute_id: int = create_attribute(definition)
        result = {
            "content": {"message": "Character created"},
            "status": status.HTTP_201_CREATED,
            "headers": {"Content-Type": "application/json", "Location": f"/character/{attribute_id}"}
        }
    else:
        for key, value in definition.items():
            attribute_data[key] = value
        update_attribute_definition(attribute_id, attribute_data)
        result = {
            "content": {"message": "Character updated"},
            "status": status.HTTP_200_OK,
            "headers": {"Content-Type": "application/json"}
        }
    return result
