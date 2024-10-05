from typing import List


class CharacterAttributeNotFound(Exception):
    def __init__(self):
        message: str = f"Character attribute not found"
        super().__init__(message)


class CharacterAttributeLinkedToResource(Exception):
    def __init__(self, resource_type: str, resource_id_list: List[int]):
        message: str = f"Character attribute linked to resource. Type: {resource_type}, Ids: {resource_id_list}"
        super().__init__(message)


class BubblesException(Exception):
    def __init__(self):
        message: str = f"Bubbles"
        super().__init__(message)
