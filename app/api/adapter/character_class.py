"""app.api.adapter.character_class module"""

from app.api.schemas.character_class import CharacterClassRequest
from app.domain.character_class import CharacterClass


def adapt_create_class_params(character_class_request: CharacterClassRequest) -> CharacterClass:
    """

    :param character_class_request:
    :return:
    """
    return CharacterClass(name=character_class_request.name)


def adapt_update_class_definition(character_class_request: CharacterClassRequest) -> CharacterClass:
    """

    :param character_class_request:
    :return:
    """
    return CharacterClass(name=character_class_request.name)
