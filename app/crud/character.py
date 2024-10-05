from typing import List

from app.crud.character_attribute import get_character_extended_attributes
from app.crud.character_class import get_character_class
from app.exceptions.character import CharacterNotFound, BubblesException
from app.models.character import Character


def get_characters_linked_to_attribute(attribute_id: int) -> List[int] | None:
    # TODO execute an SQL to check if there's a class linked to the attribute
    if attribute_id == 123:
        return [1]
    else:
        return None


def get_characters_linked_to_class(class_id: int) -> List[int] | None:
    # TODO execute an SQL to check if there's a class linked to the attribute
    if class_id == 123:
        return [1]
    else:
        return None


def get_character_by_id(character_id: int) -> Character:
    if character_id == 123:
        raise CharacterNotFound()
    elif character_id == 456:
        raise BubblesException()
    else:
        name = f"Solo mori"
        description = f"A dark elf from the far far away land"
        experience_points = 100
        character_class = get_character_class(character_id)
        character = Character(id=character_id, name=name, character_class=character_class, description=description,
                              experience_points=experience_points)
        extended_attributes = get_character_extended_attributes(character.id)
        character.character_attributes = extended_attributes
    return character


def list_all_characters() -> List[Character]:
    # TODO should add the logic to actually list all character in the DB
    character = get_character_by_id(1)
    return [character]


def search_characters_by_name(name_search: str) -> List[Character]:
    # TODO should add the logic to actually search characters by name
    name_search.capitalize()
    character = get_character_by_id(1)
    return [character]


def create_character(character: Character) -> int:
    # TODO should add the logic to actually add character to the DB
    character.id = 2
    return character.id


def delete_character_by_id(character_id: int) -> None:
    # TODO should add the logic to actually delete character in the DB
    character = get_character_by_id(character_id)


def update_character_definition(character_id: int, character_definition: Character) -> None:
    # TODO should add the logic to actually update character in the DB
    get_character_by_id(character_id)
