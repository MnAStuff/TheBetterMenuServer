from entities import Restaurant
from main import app, db
from flask_cors import cross_origin
from flask_login import login_required, current_user
from flask import request
import json


@cross_origin(origin='*')
@login_required
@app.route('/restaurant', methods=['GET'])
def get_all_restaurants():
    restaurants = Restaurant.query.filter_by(owner_id=1).all_or_404()
    dicted = map(lambda rest: rest.to_dict(), restaurants)
    return json.dumps(dicted), 200


@cross_origin(origin='*')
@login_required
@app.route('/restaurant/<restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id, owner_id=1).first_or_404()
    return json.dumps(restaurant.to_dict()), 200


@cross_origin(origin='*')
@login_required
@app.route('/restaurant', methods=['POST'])
def create_restaurant():
    body = json.loads(request.data)
    restaurant = Restaurant(body.get('name'), body.get('address'), body.get('description'), 1)
    db.session.add(restaurant)
    db.session.commit()
    return json.dumps({'restaurant_id': restaurant.id}), 200

