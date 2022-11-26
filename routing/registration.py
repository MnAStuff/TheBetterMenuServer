from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from entities import Restaurant, Menu
from entities.user import User
from entities.user_type import UserType
from main import app
from flask_cors import cross_origin
from flask import request
from flask_login import login_user
from main import db
import json


@cross_origin(origin='*')
@app.route('/registration', methods=['POST'])
def register_user():
    body = json.loads(request.data)
    try:
        user = User(body.get('login'), generate_password_hash(body.get('password')), body.get('email'), UserType.OWNER)
        db.session.add(user)
        db.session.commit()

        rest = Restaurant(body.get('login') + ' rest', 'address', 'desc', user)
        db.session.add(rest)
        db.session.commit()

        menu = Menu(rest)
        db.session.add(menu)
        db.session.commit()

        login_user(user)
        return json.dumps({'user_id': user.id, 'menu_id': menu.id})
    except IntegrityError:
        return {'result': 'User with such login or email already exist.'}, 409
