from pydantic import BaseModel


class Attribute(BaseModel):
    id: int
    name: str
    description: str
    skill_points: int
