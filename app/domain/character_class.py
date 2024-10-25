"""app.domain.character_class module"""
from typing import List
from pydantic import BaseModel


class CharacterClass(BaseModel):
    """CharacterClass Model"""
    id: int
    name: str
    attributes: List[int]
