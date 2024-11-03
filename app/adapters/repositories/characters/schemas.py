from pydantic import BaseModel, Field


class CharacterClassCreate(BaseModel):
    name: str = Field(..., description="The name of the class")
