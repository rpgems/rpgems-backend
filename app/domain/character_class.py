"""app.domain.character_class module"""
from typing import List
from pydantic import BaseModel


class CharacterClass(BaseModel):
    id: int
    name: str
    attributes: List[int]
