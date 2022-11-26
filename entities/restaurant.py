from dataclasses import dataclass
from main import db


@dataclass
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    menu = db.relationship('Menu', backref='restaurant', lazy=True)
    orders = db.relationship('Order', backref='restaurant', lazy=True)

    def __init__(self, name, address, description, owner):
        self.name = name
        self.address = address
        self.description = description
        self.owner_id = owner.id

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'name': self.name,
            'address': self.address,
            'description': self.description
        }

