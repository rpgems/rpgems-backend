from typing import List, Optional
from pydantic import BaseModel
from app.models.character_attribute import Attribute
from app.models.character_class import CharacterClass


class Character(BaseModel):
    id: int
    name: str
    character_class: CharacterClass
    description: str
    experience_points: int
    character_attributes: Optional[List[Attribute]] = None
