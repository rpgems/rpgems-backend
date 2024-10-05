from typing import List

from app.exceptions.character_attribute import CharacterAttributeNotFound, CharacterAttributeLinkedToResource, \
    BubblesException
from app.crud.character_class import get_classes_linked_to_attribute
from app.models.character import Attribute


def get_characters_linked_to_attribute(attribute_id: int) -> List[int] | None:
    # TODO execute an SQL to check if there's a class linked to the attribute
    if attribute_id == 123:
        return [1]
    else:
        return None


def get_character_extended_attributes(character_id: int) -> List[Attribute]:
    name = f"strength"
    description = f"character strength for {character_id}"
    skill_points = 50
    attribute = Attribute(id=1, name=name, description=description, skill_points=skill_points)
    result = [attribute]
    return result


def get_attribute_by_id(attribute_id: int) -> Attribute:
    if attribute_id == 123:
        raise CharacterAttributeNotFound()
    elif attribute_id == 456:
        raise BubblesException()
    else:
        name = f"Solo mori"
        description = f"A dark elf from the far far away land"
        skill_points = 100
        attribute = Attribute(id=attribute_id, name=name, description=description, skill_points=skill_points)
    return attribute


def list_all_attributes() -> List[Attribute]:
    # TODO should add the logic to actually list all character in the DB
    attribute = get_attribute_by_id(1)
    return [attribute]


def search_attributes_by_name(name_search: str) -> List[Attribute]:
    # TODO should add the logic to actually search characters by name
    name_search.capitalize()
    attribute = get_attribute_by_id(1)
    return [attribute]


def create_attribute(attribute: Attribute) -> int:
    # TODO should add the logic to actually add character to the DB
    attribute.id = 2
    return attribute.id


def delete_attribute_by_id(attribute_id: int) -> None:
    # TODO should add the logic to actually delete character in the DB
    classes_linked_to_attribute = get_classes_linked_to_attribute(attribute_id)
    if classes_linked_to_attribute is not None:
        raise CharacterAttributeLinkedToResource(resource_type="class", resource_id_list=classes_linked_to_attribute)
    characters_linked_to_attribute = get_characters_linked_to_attribute(attribute_id)
    if characters_linked_to_attribute is not None:
        raise CharacterAttributeLinkedToResource(resource_type="character",
                                                 resource_id_list=characters_linked_to_attribute)
    get_attribute_by_id(attribute_id)


def update_attribute_definition(attribute_id: int, attribute_definition: Attribute) -> None:
    # TODO should add the logic to actually update character in the DB
    attribute = get_attribute_by_id(attribute_id)
    attribute.update_attribute_definition(name=attribute_definition.name, description=attribute_definition.description,
                                          skill_points=attribute_definition.skill_points)
