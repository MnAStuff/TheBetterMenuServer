from dataclasses import dataclass
from main import db


@dataclass
class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    dish_type = db.Column(db.String(50), db.ForeignKey('dish_type.name'), nullable=True)
    enabled = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    photo_id = db.Column(db.String(200), nullable=True)

    def __init__(self, name, dish_type, description, menu, price, currency, photo_id, enabled):
        self.menu_id = menu.id
        self.enabled = False if not enabled else True
        self.name = name
        self.description = description
        self.photo_id = photo_id
        self.price = price
        self.currency = currency
        self.dish_type = dish_type

    def to_dict(self):
        return {
            'id': self.id,
            'menu_id': self.menu_id,
            'category':  self.dish_type,
            'enabled': self.enabled,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'currency': self.currency,
            'photo_id': self.photo_id
        }