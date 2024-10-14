from typing import List
from pydantic import BaseModel


class CharacterClass(BaseModel):
    id: int
    name: str
    attributes: List[int]
