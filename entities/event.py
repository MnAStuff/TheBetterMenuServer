from dataclasses import dataclass
from main import db


@dataclass
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)

    date = db.Column(db.Date, nullable=False)

    def __init__(self, restaurant, order):
        self.restaurant_id = restaurant.id
        self.order_id = order.id

    def to_dict(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'order_id': self.order_id,
            'date':  self.date
        }
