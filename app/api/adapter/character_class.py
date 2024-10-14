from typing import List

from app.api.domain.character_class import CharacterClassResponse
from app.domain.character_class import CharacterClass
from app.services.character_class import (service_get_class_by_id, service_list_classes,
                                              service_search_classes_by_name, service_create_class,
                                              service_delete_class_by_id, service_update_class_definition)


def adapt_get_class_by_id(class_id: int) -> CharacterClassResponse:
    class_response: CharacterClass = service_get_class_by_id(class_id)
    class_result = CharacterClassResponse(id=class_response.id,
                                          name=class_response.name,
                                          attributes=class_response.attributes)
    return class_result


def adapt_list_all_classes() -> List[CharacterClassResponse]:
    class_list_response: List[CharacterClass] = service_list_classes()
    class_list_result: List[CharacterClassResponse] = []
    for class_response in class_list_response:
        class_result = CharacterClassResponse(id=class_response.id,
                                              name=class_response.name,
                                              attributes=class_response.attributes)
        class_list_result.append(class_result)
    return class_list_result


def adapt_search_classes_by_name(name: str) -> List[CharacterClassResponse]:
    class_list_response: List[CharacterClass] = service_search_classes_by_name(name)
    class_list_result: List[CharacterClassResponse] = []
    for class_response in class_list_response:
        class_result = CharacterClassResponse(id=class_response.id,
                                              name=class_response.name,
                                              attributes=class_response.attributes)
        class_list_result.append(class_result)
    return class_list_result


def adapt_create_class(class_data: dict) -> int:
    class_id: int = service_create_class(class_data)
    return class_id


def adapt_delete_class_by_id(class_id: int) -> None:
    service_delete_class_by_id(class_id)


def adapt_update_class_definition(class_id: int, class_definition: dict) -> dict:
    result = service_update_class_definition(class_id, class_definition)
    return result
