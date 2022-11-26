import datetime
from entities import Restaurant, User, Order, OrderState, OrderedDish
from entities.event import Event
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
    user = User.query.filter_by(id=1).first_or_404()
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
                                            owner_id=1).first_or_404()
    mapped = map(lambda order: order.to_dict(), restaurant.orders)

    return json.dumps(mapped, indent=4)


@cross_origin(origin='*')
@app.route('/order', methods=['POST'])
def create_order():
    body = json.loads(request.data)
    ordered_dishes = body.get("positions")
    restaurant_id = body.get("restaurant_id")

    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()

    date = datetime.datetime.now()
    order = Order(OrderState.NEW, date)
    db.session.add(order)
    db.session.commit()

    if not ordered_dishes or len(ordered_dishes):
        json.dumps({'result': 'Empty order.'}, indent=4), 406

    for ordered_dish in ordered_dishes:
        db.session.add(OrderedDish(order.id, ordered_dish.dish_id, ordered_dish.count, ordered_dish.comment))
    db.session.commit()

    db.session.add(Event(restaurant, order))
    db.session.commit()

    return json.dumps({'result': 'Success'}, indent=4)


@cross_origin(origin='*')
@login_required
@app.route('/order_state', methods=['POST'])
def set_order_state():
    order = Order.query.filter_by(id=request.args.get('id')).first_or_404()
    restaurant = Restaurant.query.filter_by(id=order.restaurant_id, owner_id=1).first_or_404()

    order.state = request.args.get('state')
    db.session.commit()

    db.session.add(Event(restaurant, order))
    db.session.commit()

    return json.dumps({'result': 'Success'}, indent=4)
