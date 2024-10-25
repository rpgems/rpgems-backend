"""app.domain.character_attribute module"""
from pydantic import BaseModel


class Attribute(BaseModel):
    """Attribute model"""
    id: int
    name: str
    description: str
    skill_points: int
