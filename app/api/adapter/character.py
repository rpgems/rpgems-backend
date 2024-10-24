from typing import List

from app.api.schema.character import CharacterResponse
from app.domain.character import Character
from app.services.character import (service_get_character_by_id, service_list_characters,
                                    service_search_characters_by_name, service_create_character,
                                    service_delete_character_by_id, service_update_character_definition)


def adapt_get_character_by_id(character_id) -> CharacterResponse:
    character_response: Character = service_get_character_by_id(character_id)
    character_result = CharacterResponse(id=character_response.id,
                                         name=character_response.name,
                                         character_class=character_response.character_class,
                                         description=character_response.description,
                                         experience_points=character_response.experience_points,
                                         character_attributes=character_response.character_attributes,)
    return character_result


def adapt_list_characters() -> List[CharacterResponse]:
    character_list_response: List[Character] = service_list_characters()
    character_list_result: List[CharacterResponse] = []
    for character_response in character_list_response:
        character_result = CharacterResponse(id=character_response.id,
                                             name=character_response.name,
                                             character_class=character_response.character_class,
                                             description=character_response.description,
                                             experience_points=character_response.experience_points,
                                             character_attributes=character_response.character_attributes, )
        character_list_result.append(character_result)
    return character_list_result


def adapt_search_characters_by_name(name_search: str) -> List[CharacterResponse]:
    character_list_response: List[Character] = service_search_characters_by_name(name_search)
    character_list_result: List[CharacterResponse] = []
    for character_response in character_list_response:
        character_result = CharacterResponse(id=character_response.id,
                                             name=character_response.name,
                                             character_class=character_response.character_class,
                                             description=character_response.description,
                                             experience_points=character_response.experience_points,
                                             character_attributes=character_response.character_attributes, )
        character_list_result.append(character_result)
    return character_list_result


def adapt_create_character(character_data: dict) -> int:
    character_id: int = service_create_character(character_data)
    return character_id


def adapt_delete_character_by_id(character_id: int) -> None:
    service_delete_character_by_id(character_id)


def adapt_update_character_definition(character_id: int, character_definition: dict) -> dict:
    result = service_update_character_definition(character_id, character_definition)
    return result
