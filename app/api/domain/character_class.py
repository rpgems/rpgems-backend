from typing import List

from pydantic import BaseModel


class CharacterClassResponse(BaseModel):
    id: int
    name: str
    attributes: List[int]
