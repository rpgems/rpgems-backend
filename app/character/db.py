from app.character.exceptions import CharacterNotFound, BubblesException
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
