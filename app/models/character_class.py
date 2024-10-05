from typing import List
from pydantic import BaseModel
from app.models.character_attribute import Attribute


class CharacterClass(BaseModel):
    id: int
    name: str
    attributes: List[Attribute]

    def update_character_class_definition(self, name: str, attributes: List[Attribute]):
        self.name = name
        self.attributes = attributes
