from typing import List

from app.api.schema.character_attribute import CharacterAttributeResponse
from app.domain.character_attribute import Attribute
from app.services.character_attribute import (service_get_attribute_by_id, service_list_attributes,
                                              service_search_attributes_by_name, service_create_attribute,
                                              service_delete_attribute_by_id, service_update_attribute_definition)


def adapt_get_attribute_by_id(attribute_id: int) -> CharacterAttributeResponse:
    attribute_response: Attribute = service_get_attribute_by_id(attribute_id)
    attribute_result = CharacterAttributeResponse(id=attribute_response.id,
                                                  name=attribute_response.name,
                                                  description=attribute_response.description,
                                                  skill_points=attribute_response.skill_points,)
    return attribute_result


def adapt_list_all_attributes() -> List[CharacterAttributeResponse]:
    attribute_list_response: List[Attribute] = service_list_attributes()
    attribute_list_result: List[CharacterAttributeResponse] = []
    for attribute_response in attribute_list_response:
        attribute_result = CharacterAttributeResponse(id=attribute_response.id,
                                                      name=attribute_response.name,
                                                      description=attribute_response.description,
                                                      skill_points=attribute_response.skill_points)
        attribute_list_result.append(attribute_result)
    return attribute_list_result


def adapt_search_attributes_by_name(name: str) -> List[CharacterAttributeResponse]:
    attribute_list_response: List[Attribute] = service_search_attributes_by_name(name)
    attribute_list_result: List[CharacterAttributeResponse] = []
    for attribute_response in attribute_list_response:
        attribute_result = CharacterAttributeResponse(id=attribute_response.id,
                                                      name=attribute_response.name,
                                                      description=attribute_response.description,
                                                      skill_points=attribute_response.skill_points)
        attribute_list_result.append(attribute_result)
    return attribute_list_result


def adapt_create_attribute(attribute_data: dict) -> int:
    attribute_id: int = service_create_attribute(attribute_data)
    return attribute_id


def adapt_delete_attribute_by_id(attribute_id: int) -> None:
    service_delete_attribute_by_id(attribute_id)


def adapt_update_attribute_definition(attribute_id: int, attribute_definition: dict) -> dict:
    result = service_update_attribute_definition(attribute_id, attribute_definition)
    return result
