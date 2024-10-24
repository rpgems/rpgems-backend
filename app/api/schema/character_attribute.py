"""app.api.domain.character_attribute module"""
from pydantic import BaseModel


class CharacterAttributeResponse(BaseModel):
    """CharacterAttributeResponse model"""
    id: int
    name: str
    description: str
    skill_points: int
