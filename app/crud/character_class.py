from typing import List

from app.crud.character import get_characters_linked_to_class
from app.crud.character_attribute import get_character_class_attributes, get_character_extended_attributes
from app.exceptions.character_class import CharacterClassNotFound, CharacterClassLinkedToResource, BubblesException
from app.models.character_class import CharacterClass


def get_classes_linked_to_attribute(attribute_id: int) -> List[int] | None:
    # TODO execute an SQL to check if there's a class linked to the attribute
    if attribute_id == 123:
        return [1]
    else:
        return None


def get_character_class(character_id: int) -> CharacterClass:
    character_class_id = 1
    name = f"Elf {character_id}"
    class_attributes = get_character_class_attributes(character_class_id)
    character_class = CharacterClass(id=character_class_id, name=name, attributes=class_attributes)
    return character_class


def get_class_by_id(class_id: int) -> CharacterClass:
    if class_id == 123:
        raise CharacterClassNotFound()
    elif class_id == 456:
        raise BubblesException()
    else:
        name = f"Solo mori"
        character_class = CharacterClass(id=class_id, name=name, attributes=get_character_extended_attributes(class_id))
    return character_class


def list_all_classes() -> List[CharacterClass]:
    # TODO should add the logic to actually list all character in the DB
    character_class = get_class_by_id(1)
    return [character_class]


def search_classes_by_name(name_search: str) -> List[CharacterClass]:
    # TODO should add the logic to actually search characters by name
    name_search.capitalize()
    character_class = get_class_by_id(1)
    return [character_class]


def create_class(character_class: CharacterClass) -> int:
    # TODO should add the logic to actually add character to the DB
    character_class.id = 2
    return character_class.id


def delete_class_by_id(class_id: int) -> None:
    # TODO should add the logic to actually delete character in the DB
    attributes = get_character_class_attributes(class_id)
    if attributes is not None:
        raise CharacterClassLinkedToResource(resource_type="attribute",
                                             resource_id_list=[attribute.id for attribute in attributes])
    characters = get_characters_linked_to_class(class_id)
    if characters is not None:
        raise CharacterClassLinkedToResource(resource_type="character", resource_id_list=characters)
    get_class_by_id(class_id)


def update_class_definition(class_id: int, class_definition: CharacterClass) -> None:
    # TODO should add the logic to actually update character in the DB
    character_class = get_class_by_id(class_id)
    character_class.update(name=class_definition.name, attributes=class_definition.attributes)
