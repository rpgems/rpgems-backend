class CharacterNotFound(Exception):
    def __init__(self):
        message: str = f"Character not found"
        super().__init__(message)


class BubblesException(Exception):
    def __init__(self):
        message: str = f"Bubbles"
        super().__init__(message)
