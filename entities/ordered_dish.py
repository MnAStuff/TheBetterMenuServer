from sqlalchemy.orm import backref

from main import db


class OrderedDish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(200))

    dish = db.relationship('Dish', lazy=False, backref=backref('dish_id', lazy='dynamic'))

    def __init__(self, order_id, dish_id, count, comment):
        self.order_id = order_id
        self.dish_id = dish_id
        self.count = count
        self.comment = comment

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'dish': self.dish.to_dict(),
            'comment': self.comment,
            'count': self.count
        }
