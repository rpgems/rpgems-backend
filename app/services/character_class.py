"""app.services.character_class module"""
from typing import List

from fastapi import HTTPException
from starlette import status

from app.domain.character_class import CharacterClass
from app.repository.sql.character_class import (get_class_by_id, list_all_classes, search_classes_by_name, create_class,
                                                delete_class_by_id, update_class_definition)


def service_get_class_by_id(class_id: int) -> CharacterClass:
    """

    :param class_id:
    :return:
    """
    if isinstance(class_id, int):
        class_response: dict = get_class_by_id(class_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="class_id should be a number")
    if class_response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="class not found")
    character_class = CharacterClass()
    character_class.id = class_id
    character_class.name = class_response['name']
    character_class.attributes = class_response['attributes']
    return character_class


def service_list_classes() -> List[CharacterClass]:
    """

    :return:
    """
    class_list_data: List[dict] = list_all_classes()
    if len(class_list_data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No classes found")
    class_list: List[CharacterClass] = []
    for class_data in class_list_data:
        character_class: CharacterClass = CharacterClass()
        character_class.id = class_data["id"]
        character_class.name = class_data["name"]
        character_class.attributes = class_data["attributes"]
        class_list.append(character_class)
    return class_list


def service_search_classes_by_name(name: str) -> List[CharacterClass]:
    """

    :param name:
    :return:
    """
    if len(name) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name should be a non-empty string")
    class_list_data: List[dict] = search_classes_by_name(name)
    if len(class_list_data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No classes found")
    class_list: List[CharacterClass] = []
    for class_data in class_list_data:
        character_class: CharacterClass = CharacterClass()
        character_class.id = class_data["id"]
        character_class.name = class_data["name"]
        character_class.attributes = class_data["attributes"]
        class_list.append(character_class)
    return class_list


def service_create_class(class_data: dict) -> int:
    """

    :param class_data:
    :return:
    """
    keys = ["name", "attributes"]
    if all(key in keys for key in class_data.keys()):
        class_id: int = create_class(class_data)
    else:
        missing_fields = list(set(keys) - set(class_data.keys()))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Missing required fields: {missing_fields}")
    return class_id


def service_delete_class_by_id(class_id: int) -> None:
    """

    :param class_id:
    """
    if isinstance(class_id, int):
        class_data: dict = get_class_by_id(class_id)
        if class_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")
        delete_class_by_id(class_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Class id should be a number")


def service_update_class_definition(class_id: int, definition: dict) -> dict:
    """

    :param class_id:
    :param definition:
    :return:
    """
    keys = ["name", "attributes"]
    if not isinstance(class_id, int):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Class id should be a number")
    if not definition.keys() in keys:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"malformed keys: {definition.keys()}")
    class_data: dict = get_class_by_id(class_id)
    if class_data is None:
        class_id: int = create_class(definition)
        result = {
            "content": {"message": "Class created"},
            "status": status.HTTP_201_CREATED,
            "headers": {"Content-Type": "application/json", "Location": f"/character/{class_id}"}
        }
    else:
        for key, value in definition.items():
            class_data[key] = value
        update_class_definition(class_id, class_data)
        result = {
            "content": {"message": "Class updated"},
            "status": status.HTTP_200_OK,
            "headers": {"Content-Type": "application/json"}
        }
    return result
