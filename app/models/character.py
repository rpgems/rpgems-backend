from typing import List, Optional

from pydantic import BaseModel


class Attribute(BaseModel):
    id: int
    name: str
    description: str
    skill_points: int


class CharacterClass(BaseModel):
    id: int
    name: str
    attributes: List[Attribute]


class Character(BaseModel):
    id: int
    name: str
    character_class: CharacterClass
    description: str
    experience_points: int
    character_attributes: Optional[List[Attribute]] = None
