from pydantic import BaseModel


class Attribute(BaseModel):
    id: int
    name: str
    description: str
    skill_points: int

    def update_attribute_definition(self, name: str, description: str, skill_points: int):
        self.name = name
        self.description = description
        self.skill_points = skill_points
