from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import Optional
from sqlalchemy import ForeignKey

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance: Mapped[int]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    
    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["distance"] = self.distance

        if self.moons:
            planet_as_dict["moons"] = [
                moon.to_dict() for moon in self.moons
                ]

        return planet_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = cls(name=planet_data["name"],
                        description=planet_data["description"],
                        distance=planet_data["distance"])
                        
        return new_planet
    
    
# class Planet:
#     def __init__(self, id, name, description, distance):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance = distance

# planets = [
#     Planet(1, "Earth", "The third planet from the Sun.", 0),
#     Planet(2, "Mars", "The fourth planet from the Sun.", 225),
#     Planet(3, "Jupiter", "The fifth planet from the Sun.", 778)
# ]

