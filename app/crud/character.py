from typing import List

from app.exceptions.character import CharacterNotFound, BubblesException
from app.character.model import Character, CharacterClass, Attribute


def get_character_class_attributes(class_id: int) -> list:
    name = f"strength"
    description = f"character strength"
    skill_points = 50
    attribute = Attribute(id=1, name=name, description=description, skill_points=skill_points)
    result = [attribute]
    return result


def get_character_extended_attributes(character_id: int) -> list:
    name = f"strength"
    description = f"character strength"
    skill_points = 50
    attribute = Attribute(id=1, name=name, description=description, skill_points=skill_points)
    result = [attribute]
    return result


def get_character_class(character_id: int) -> CharacterClass:
    character_class_id = 1
    name = f"Elf"
    class_attributes = get_character_class_attributes(character_class_id)
    character_class = CharacterClass(id=character_class_id, name=name, attributes=class_attributes)
    return character_class


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
    character = get_character_by_id(1)
    return [character]


def create_character(character: Character) -> int:
    # TODO should add the logic to actually add character to the DB
    return 2


def delete_character_by_id(character_id: int) -> None:
    # TODO should add the logic to actually delete character in the DB
    character = get_character_by_id(character_id)


def update_character_definition(character_id: int, character_definition: Character) -> None:
    # TODO should add the logic to actually update character in the DB
    get_character_by_id(character_id)
