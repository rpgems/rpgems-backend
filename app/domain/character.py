"""app.domain.character module"""
from typing import List, Optional
from pydantic import BaseModel


class Character(BaseModel):
    """Character model"""
    id: int
    name: str
    character_class: int
    description: str
    experience_points: int
    character_attributes: Optional[List[int]] = None
