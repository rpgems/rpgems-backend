"""app.api.domain.character_class module"""

from typing import List

from pydantic import BaseModel


class CharacterClassRequest(BaseModel):
    """
    CharacterClassRequest model
    """
    name: str


class CharacterClassResponse(BaseModel):
    """CharacterClassResponse model"""

    uuid: str
    name: str
    attributes: List[int] | None = None

    def to_dict(self) -> dict:
        """
        Return dict representation of Character Class
        :return: dict representation of Character Class
        """
        return {
            "uuid": self.uuid,
            "name": self.name,
            "attributes": self.attributes
        }
