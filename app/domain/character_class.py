"""app.domain.character_class module"""

from typing import List
from uuid import UUID
from pydantic import BaseModel


class CharacterClass(BaseModel):
    """CharacterClass Model"""

    uuid: UUID | None = None
    name: str
    attributes: List[str] | None = None

    def to_dict(self) -> dict:
        """
        Create a dictionary representation of the CharacterClass class
        """
        character_class_dict = {"uuid": self.uuid, "name": self.name, "attributes": self.attributes}
        return character_class_dict
