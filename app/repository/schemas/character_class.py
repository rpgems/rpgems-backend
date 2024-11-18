"""
app.repository.schemas module
"""
from pydantic import BaseModel, Field


class CharacterClass(BaseModel):
    name: str = Field(..., description="The name of the class")
