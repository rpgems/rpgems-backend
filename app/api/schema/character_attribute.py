from pydantic import BaseModel


class CharacterAttributeResponse(BaseModel):
    id: int
    name: str
    description: str
    skill_points: int
