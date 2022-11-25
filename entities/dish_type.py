from dataclasses import dataclass
from main import db


@dataclass
class DishType(db.Model):
    name = db.Column(db.String(50), primary_key=True)

    def __init__(self, name):
        self.name = name

