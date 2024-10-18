"""app.api.adapter.character module"""
from typing import List

from app.api.domain.character import CharacterResponse
from app.domain.character import Character
from app.services.character import (service_get_character_by_id, service_list_characters,
                                    service_search_characters_by_name, service_create_character,
                                    service_delete_character_by_id,
                                    service_update_character_definition)


def adapt_get_character_by_id(character_id) -> CharacterResponse:
    """

    :param character_id:
    :return:
    """
    char_response: Character = service_get_character_by_id(character_id)
    character_result = CharacterResponse(id=char_response.id,
                                         name=char_response.name,
                                         character_class=char_response.character_class,
                                         description=char_response.description,
                                         experience_points=char_response.experience_points,
                                         character_attributes=char_response.character_attributes)
    return character_result


def adapt_list_characters() -> List[CharacterResponse]:
    """

    :return:
    """
    character_list_response: List[Character] = service_list_characters()
    character_list_result: List[CharacterResponse] = []
    for char_resp in character_list_response:
        character_result = CharacterResponse(id=char_resp.id,
                                             name=char_resp.name,
                                             character_class=char_resp.character_class,
                                             description=char_resp.description,
                                             experience_points=char_resp.experience_points,
                                             character_attributes=char_resp.character_attributes)
        character_list_result.append(character_result)
    return character_list_result


def adapt_search_characters_by_name(name_search: str) -> List[CharacterResponse]:
    """

    :param name_search:
    :return:
    """
    character_list_response: List[Character] = service_search_characters_by_name(name_search)
    character_list_result: List[CharacterResponse] = []
    for char_resp in character_list_response:
        character_result = CharacterResponse(id=char_resp.id,
                                             name=char_resp.name,
                                             character_class=char_resp.character_class,
                                             description=char_resp.description,
                                             experience_points=char_resp.experience_points,
                                             character_attributes=char_resp.character_attributes)
        character_list_result.append(character_result)
    return character_list_result


def adapt_create_character(character_data: dict) -> int:
    """

    :param character_data:
    :return:
    """
    character_id: int = service_create_character(character_data)
    return character_id


def adapt_delete_character_by_id(character_id: int) -> None:
    """

    :param character_id:
    """
    service_delete_character_by_id(character_id)


def adapt_update_character_definition(character_id: int, character_definition: dict) -> dict:
    """

    :param character_id:
    :param character_definition:
    :return:
    """
    result = service_update_character_definition(character_id, character_definition)
    return result
