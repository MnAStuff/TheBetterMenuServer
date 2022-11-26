import datetime
from entities import Restaurant, User, Order, OrderState, OrderedDish
from entities.menu import Menu
from main import app, db
from flask_cors import cross_origin
from flask_login import login_required, current_user
from flask import request
import json


@cross_origin(origin='*')
@login_required
@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    user = User.query.filter_by(id=current_user.id).first_or_404()
    order = None
    for rest in user.restaurants:
        for ord in rest.orders:
            if ord.id == order_id:
                order = ord
                break
        if order:
            break

    if not order:
        return json.dumps({'result': 'You do not have access to this resource'}, indent=4), 404

    return json.dumps(order.to_dict(), indent=4)


@cross_origin(origin='*')
@login_required
@app.route('/order', methods=['GET'])
def get_all_orders():
    restaurant = Restaurant.query.filter_by(id=request.args.get('restaurant_id'),
                                            owner_id=current_user.id).first_or_404()
    mapped = map(lambda order: order.to_dict(), restaurant.orders)

    return json.dumps(mapped, indent=4)


@cross_origin(origin='*')
@app.route('/order', methods=['POST'])
def create_order():
    body = json.loads(request.data)

    order = Order(OrderState.NEW, datetime.datetime.now())
    db.session.add(order)

    ordered_dishes = body.get("positions")
    if not ordered_dishes or len(ordered_dishes):
        json.dumps({'result': 'You do not have access to this resource'}, indent=4), 401

    for ordered_dish in ordered_dishes:
        db.session.add(OrderedDish(order.id, ordered_dish.dish_id, ordered_dish.count, ordered_dish.comment))
    db.session.commit()

    return json.dumps({'result': 'Success'}, indent=4)
