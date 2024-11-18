"""app.api.domain.character_class module"""

from typing import List
from uuid import UUID

from pydantic import BaseModel


class CharacterClassRequest(BaseModel):
    """
    CharacterClassRequest model
    """
    name: str


class CharacterClassResponse(BaseModel):
    """CharacterClassResponse model"""

    uuid: UUID
    name: str
    attributes: List[int] | None = None
