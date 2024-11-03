"""app.domain.character module"""

from typing import List, Optional
from pydantic import BaseModel

from app.domain.character_class import CharacterClass


class Character(BaseModel):
    """Character model"""

    id: int
    name: str
    character_class: int | CharacterClass
    description: str
    experience_points: int
    character_attributes: Optional[List[int]] = None
