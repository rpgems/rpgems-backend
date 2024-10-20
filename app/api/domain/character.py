from typing import Optional, List

from pydantic import BaseModel


class CharacterResponse(BaseModel):
    id: int
    name: str
    character_class: int
    description: str
    experience_points: int
    character_attributes: Optional[List[int]]
