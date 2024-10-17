from typing import List


def _adapt_list_response(list_of_attributes: List[dict]) -> List[dict]:
    result = []
    if len(list_of_attributes) != 0:
        for attribute in list_of_attributes:
            attribute_result = {
                "id": attribute,
                "name": "attribute['name']",
                "description": "attribute['description']",
                "skill_points": "attribute['skill_points']"
            }
            result.append(attribute_result)
    return result


def get_character_extended_attributes(character_id: int) -> List[dict]:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT attribute_id FROM character_attributes WHERE character_id = {character_id}"
    query_expression.capitalize()
    list_of_attribute_ids = [1, 2, 3]  # executed query_expression
    result = []
    for attribute_id in list_of_attribute_ids:
        attribute = get_attribute_by_id(attribute_id)
        result.append(attribute)
    return result


def get_attribute_by_id(attribute_id: int) -> dict | None:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM attribute WHERE id = {attribute_id}"
    query_result = query_expression
    if len(query_result) == 0:
        attribute = None
    else:
        attribute = {
            "id": attribute_id,
            "name": f"Solo mori",
            "description": f"A dark elf from the far far away land",
            "skill_points": 100
        }
    return attribute


def list_all_attributes() -> List[dict]:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM attribute"
    query_expression.capitalize()
    list_of_attributes = [{}]
    return _adapt_list_response(list_of_attributes)


def search_attributes_by_name(name_search: str) -> List[dict]:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM attribute WHERE name LIKE '{name_search}%'"
    query_expression.capitalize()
    list_of_attributes = [{}]
    return _adapt_list_response(list_of_attributes)


def create_attribute(attribute: dict) -> int:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = (f"INSERT INTO attribute (name, description, skill_points) values ('{attribute['name']}', "
                        f"'{attribute['description']}', '{attribute['skill_points']})' RETURNING id")
    query_result = query_expression
    if query_result is None:
        result = 0
    else:
        result = query_result[0]
    return result


def delete_attribute_by_id(attribute_id: int) -> None:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"DELETE FROM attribute where id = {attribute_id}"
    query_expression.capitalize()


def update_attribute_definition(attribute_id: int, attribute_definition: dict) -> None:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = (f"UPDATE attribute set name='{attribute_definition['name']}',"
                        f" description={attribute_definition['description']},"
                        f" skill_points={attribute_definition['skill_points']} WHERE id={attribute_id}")
    query_expression.capitalize()
