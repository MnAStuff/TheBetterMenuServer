from dataclasses import dataclass
from main import db


@dataclass
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    state = db.Column(db.String, db.ForeignKey('order_state.name'), nullable=False)
    date = db.Column(db.Date, nullable=False)

    ordered_dishes = db.relationship('OrderedDish', backref='ordered_dish', lazy=False)

    def __init__(self, state, date):
        self.state = state
        self.date = date

    def to_dict(self):
        return {
            'id': self.id,
            'state': self.state,
            'date': self.date,
            'ordered_dishes': [ordered_dish.to_dict() for ordered_dish in self.ordered_dishes]
        }
