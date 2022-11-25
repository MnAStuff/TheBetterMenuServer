from entities import Restaurant
from entities.menu import Menu
from main import app
from flask_cors import cross_origin
from flask_login import login_required, current_user
from flask import request
import json


@cross_origin(origin='*')
@app.route('/menu/<menu_id>', methods=['GET'])
def get_menu(menu_id):
    menu = Menu.query.filter_by(id=menu_id).first_or_404()
    print(menu.to_dict())
    return json.dumps(menu.to_dict(), indent=4)

@cross_origin(origin='*')
@login_required
@app.route('/menu', methods=['GET'])
def get_all_menu():
    if Restaurant.query.filter_by(id=request.args.get('restaurant_id'), owner_id=current_user.id).first:
        all_menu = Menu.query.filter_by(restaurant_id=request.args.get('restaurant_id')).all_or_404()
        return json.dumps([menu.to_dict() for menu in all_menu], indent=4)
    return json.dumps({'result': 'You do not have access to this resource'}, indent=4), 404
