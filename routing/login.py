from entities import Restaurant
from entities.user import User
from main import app
from flask_cors import cross_origin
from flask import request
import json
from flask_login import login_user
from werkzeug.security import check_password_hash


@cross_origin(origin='*')
@app.route('/login', methods=['POST'])
def login():
    body = json.loads(request.data)
    user = User.query.filter_by(login=body.get('login')).first()
    # remember = True if request.form.get('remember') else False

    if not user or not check_password_hash(user.password, body.get('password')):
        return json.dumps({'result': 'Wrong login or password'}), 401
    print(login_user(user))

    restaurant = Restaurant.query.filter_by(owner_id=user.id).first_or_404()

    return json.dumps({'user_id': user.id, 'menu_id': restaurant.menu[0].id}), 200

