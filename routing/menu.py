from entities import Restaurant, Dish
from entities.menu import Menu
from main import app, db
from flask_cors import cross_origin
from flask_login import login_required, current_user
from flask import request
import json


@cross_origin(origin='*')
@app.route('/menu/<menu_id>', methods=['GET'])
def get_menu(menu_id):
    menu = Menu.query.filter_by(id=menu_id).first_or_404()
    return json.dumps(menu.to_dict(), indent=4)


@cross_origin(origin='*')
@login_required
@app.route('/menu', methods=['GET'])
def get_all_menu():
    if Restaurant.query.filter_by(id=request.args.get('restaurant_id'), owner_id=current_user.id).first:
        all_menu = Menu.query.filter_by(restaurant_id=request.args.get('restaurant_id')).all_or_404()
        return json.dumps([menu.to_dict() for menu in all_menu], indent=4)
    return json.dumps({'result': 'You do not have access to this resource'}, indent=4), 404


@cross_origin(origin='*')
@login_required
@app.route('/menu', methods=['POST'])
def create_menu():
    body = json.loads(request.data)
    restaurant_id = body.get('body')
    dishes = body.get('dishes')

    Restaurant.query.filter_by(id=restaurant_id, owner_id=current_user.id).first_or_404()

    menu = Menu(restaurant_id)
    db.session.add(menu)
    db.session.commit()

    for dish in dishes:
        db.session.add(Dish(dish.name, dish.dish_type, dish.description, menu, dish.price, dish.currency, dish.photo_id, dish.enabled))
    db.session.commit()

    return json.dumps({'manu_id': menu.id}, indent=4)
