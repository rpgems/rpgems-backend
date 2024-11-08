"""app.repository.sql module"""

import json
from typing import List


def generic_get_by_id(table_name: str, entity_id: int) -> dict | None:
    """

    :param table_name:
    :param entity_id:
    :return:
    """
    query_expression = f"SELECT * FROM {table_name} WHERE id = {entity_id}"
    query_result = query_expression
    if len(query_result) == 0:
        entity = None
    else:
        # TODO return None until sql is set
        entity = None
    return entity


def generic_list(table_name: str) -> List[dict]:
    """

    :param table_name:
    :return:
    """
    query_expression = f"SELECT * FROM {table_name}"
    entity_list = [{"result": query_expression}]
    return entity_list


def generic_search_by_name(table_name: str, entity_name: str) -> List[dict]:
    """

    :param table_name:
    :param entity_name:
    :return:
    """
    query_expression = f"SELECT * FROM {table_name} WHERE name LIKE '{entity_name}%'"
    entity_list = [{"result": query_expression}]
    return entity_list


def generic_search(
    table_name: str, column_result: str, column_search: str, column_value: any
) -> (List)[dict]:
    """ "

    :param table_name:
    :param column_result:
    :param column_search:
    :param column_value:
    :return:
    """
    query_expression = (
        f"SELECT {column_result} FROM {table_name} WHERE {column_search} ="
        f" {column_value}"
    )
    result = [{"result": query_expression}]
    return result


def generic_create(table_name: str, entity: dict) -> int:
    """

    :param table_name:
    :param entity:
    :return:
    """
    query_expression = (
        f"INSERT INTO {table_name} VALUES {json.dumps(entity)} RETURNING id"
    )
    query_result = query_expression
    if query_result is None:
        result = 0
    else:
        result = query_result[0]
    return result


def generic_delete_by_id(table_name: str, entity_id: int) -> None:
    """

    :param table_name:
    :param entity_id:
    :return:
    """
    query_expression = f"DELETE FROM {table_name} WHERE id = {entity_id}"
    query_expression.capitalize()


def generic_update(table_name: str, entity_id: int, entity: dict) -> None:
    """

    :param table_name:
    :param entity_id:
    :param entity:
    :return:
    """
    query_expression = (
        f"UPDATE {table_name} SET {json.dumps(entity)} WHERE id = {entity_id}"
    )
    query_expression.capitalize()
