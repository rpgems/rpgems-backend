from typing import List


def _adapt_list_response(list_of_characters: List[dict]) -> List[dict]:
    result = []
    if len(list_of_characters) != 0:
        for character in list_of_characters:
            character_result = {
                "id": character,
                "name": "character['name']",
                "class": "character['class']",
                "description": "character['description']",
                "experience_points": "character['experience_points']"
            }
            result.append(character_result)
    return result


def get_characters_linked_to_attribute(attribute_id: int) -> List[dict]:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT character_id FROM character_attributes WHERE attribute_id = {attribute_id}"
    query_expression.capitalize()
    list_of_character_ids = [1, 2, 3]
    result = []
    if len(list_of_character_ids) != 0:
        for character_id in list_of_character_ids:
            character = get_character_by_id(character_id)
            result.append(character)
    return result


def get_characters_linked_to_class(class_id: int) -> List[dict]:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM character WHERE class={class_id}"
    query_expression.capitalize()
    list_of_characters = [{}]
    return _adapt_list_response(list_of_characters)


def get_character_by_id(character_id: int) -> dict | None:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM character WHERE character_id = {character_id}"
    query_result = query_expression
    if len(query_result) == 0:
        return None
    else:
        character = {
            "id": "query_result['id']",
            "name": "query_result['name']",
            "class": "query_result['class']",
            "description": "query_result['description']",
            "experience_points": "query_result['experience_points']",
            "attributes": "query_result['character_attributes']"
        }
        return character


def list_all_characters() -> List[dict]:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM character"
    query_expression.capitalize()
    list_of_characters = [{}]
    return _adapt_list_response(list_of_characters)


def search_characters_by_name(name_search: str) -> List[dict]:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"SELECT * FROM character WHERE name LIKE '{name_search}%'"
    query_expression.capitalize()
    list_of_characters = [{}]
    return _adapt_list_response(list_of_characters)


def create_character(character: dict) -> int:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = (f"INSERT INTO character (name, class, description, experience_points) VALUES "
                        f"({character['name']}, {character['class']}, {character['description']}, "
                        f"{character['experience_points']}) RETURNING id")
    query_result = query_expression
    if query_result is None:
        result = 0
    else:
        result = query_result[0]
        for attribute_id in character['attributes']:
            query_expression = f"INSERT INTO attribute (character_id, attribute_id) VALUES ({result}, {attribute_id})"
            query_expression.capitalize()
    return result


def delete_character_by_id(character_id: int) -> None:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = f"DELETE FROM character WHERE id = {character_id}"
    query_expression.capitalize()


def update_character_definition(character_id: int, character_definition: dict) -> None:
    # TODO Add the function that execute the query_expression on the DB
    query_expression = (f"UPDATE character SET name = {character_definition['name']}, "
                        f"class = {character_definition['class']}, description = {character_definition['description']},"
                        f" experience_points = {character_definition['experience_points']} WHERE id = {character_id}")
    query_expression.capitalize()
