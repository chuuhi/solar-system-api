from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance: Mapped[int]
    
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

