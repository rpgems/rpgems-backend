"""app.repository.sql.character_class module"""
from typing import List


def _adapt_list_response(list_of_classes: List[dict]) -> List[dict]:
    result = []
    if len(list_of_classes) != 0:
        for character_class in list_of_classes:
            class_result = {
                "id": character_class,
                "name": "character_class['name']"
            }
            result.append(class_result)
    return result


def get_classes_linked_to_attribute(attribute_id: int) -> List[dict]:
    """

    :param attribute_id:
    :return:
    """
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT class_id FROM class_attributes WHERE attribute_id = {attribute_id}"
    query_expression.capitalize()
    list_of_class_ids = [1, 2, 3]
    result = []
    if len(list_of_class_ids) != 0:
        for class_id in list_of_class_ids:
            character_class = get_class_by_id(class_id)
            result.append(character_class)
    return result


def get_character_class(character_id: int) -> dict | None:
    """

    :param character_id:
    :return:
    """
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT class FROM character WHERE id = {character_id}"
    query_expression.capitalize()
    class_id = 1
    character_class = get_class_by_id(class_id)
    return character_class


def get_class_by_id(class_id: int) -> dict | None:
    """

    :param class_id:
    :return:
    """
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM class where id = {class_id}"
    query_result = query_expression
    if len(query_result) == 0:
        return None
    character_class = {
        "id": "query_result['id']",
        "name": "query_result['name']"
    }
    return character_class


def list_all_classes() -> List[dict]:
    """

    :return:
    """
    # TODO Add the function that execute the query_expression on the DB
    query_expression = "SELECT * FROM class"
    query_expression.capitalize()
    list_of_classes = [{}]
    return _adapt_list_response(list_of_classes)


def search_classes_by_name(name_search: str) -> List[dict]:
    """

    :param name_search:
    :return:
    """
    # TODO should add the logic to actually search characters by name
    query_expression = f"SELECT * FROM class where name LIKE '{name_search}%'"
    query_expression.capitalize()
    list_of_classes = [{}]
    return _adapt_list_response(list_of_classes)


def create_class(character_class: dict) -> int:
    """

    :param character_class:
    :return:
    """
    # TODO should add the logic to actually add character to the DB
    query_expression = f"INSERT INTO class (name) values ('{character_class['name']}' RETURNING id"
    query_result = query_expression
    if query_result is None:
        result = 0
    else:
        result = query_result[0]
    return result


def delete_class_by_id(class_id: int) -> None:
    """

    :param class_id:
    """
    # TODO should add the logic to actually delete character in the DB
    query_expression = f"DELETE FROM class where id = {class_id}"
    query_expression.capitalize()


def update_class_definition(class_id: int, class_definition: dict) -> None:
    """

    :param class_id:
    :param class_definition:
    """
    # TODO should add the logic to actually update character in the DB
    query_expression = f"UPDATE class SET name = {class_definition['name']} WHERE id = {class_id}"
    query_expression.capitalize()
