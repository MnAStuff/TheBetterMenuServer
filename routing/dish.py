from entities import User, Menu, Restaurant, Dish, DishType
from main import app, db
from flask_cors import cross_origin
from flask_login import login_required, current_user
from flask import request
import json


@cross_origin(origin='*')
@login_required
@app.route('/dish', methods=['UPDATE'])
def update_dish():
    body = json.loads(request.data)

    user = User.query.filter_by(id=1).first_or_404()
    user_dishes = []
    for rest in user.restaurants:
        for menu in rest.menu:
            for dish in menu.dishes:
                user_dishes.append(dish)
    filtered_dish = list(filter(lambda dish: dish.id == body.get('id'), user_dishes))
    if len(filtered_dish) == 0:
        return json.dumps({'result': 'You do not have access to this resource'}, indent=4), 404
    dish = filtered_dish[0]

    for k, v in dish.__dict__:
        dish[k] = body.get(k)
    db.session.commit()

    return json.dumps({'result': 'Success', 'updated_item': dish.to_dict()})


@cross_origin(origin='*')
@login_required
@app.route('/dish', methods=['POST'])
def create_dish():
    body = json.loads(request.data)

    menu = Menu.query.filter_by(id=body.get('menu_id')).first_or_404()
    Restaurant.query.filter_by(id=menu.id, owner_id=1).first_or_404()

    category = DishType.query.filter_by(name=body.get('category')).first()
    if not category:
        db.session.add(DishType(body.get('category')))
        db.session.commit()

    dish = Dish(body.get('name'), body.get('category'), body.get('description'), menu, body.get('price'), body.get('currency'), body.get('image'),
         body.get('enabled'))
    db.session.add(dish)
    db.session.commit()

    return json.dumps(dish.to_dict(), indent=4)

@cross_origin(origin='*')
@login_required
@app.route('/dish/<dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    body = json.loads(request.data)

    menu = Menu.query.filter_by(id=body.get('menu_id')).first_or_404()
    Restaurant.query.filter_by(id=menu.id, owner_id=1).first_or_404()

    dish = Dish.query.filter_by(id=dish_id).first_or_404()
    dish.menu_id = None
    db.session.commit()

    return json.dumps({'result': 'Success'}, indent=4)

