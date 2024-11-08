"""app.api.domain.character_class module"""

from typing import List

from pydantic import BaseModel


class CharacterClassRequest(BaseModel):
    name: str


class CharacterClassResponse(BaseModel):
    """CharacterClassResponse model"""

    id: int
    name: str
    attributes: List[int] = []
