from dataclasses import dataclass
from main import db


@dataclass
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    dishes = db.relationship('Dish', backref='menu', lazy=True)

    def __init__(self, restaurant):
        self.restaurant_id = restaurant.id

    def to_dict(self):
        dishes_by_category = {}
        for dish in self.dishes:
            if not dishes_by_category.get(dish.dish_type):
                dishes_by_category[dish.dish_type] = [dish.to_dict()]
            else:
                dishes_by_category[dish.dish_type].append(dish.to_dict())

        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'dishes':  dishes_by_category
        }
