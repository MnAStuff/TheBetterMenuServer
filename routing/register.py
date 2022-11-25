from entities.user import User
from entities.user_type import UserType
from main import app
from flask_cors import cross_origin
from flask import request
from main import db


@cross_origin(origin='*')
@app.route('/register')
def register_user():
    body = request.form
    try:
        user = User(body.get('login'), body.get('password'), body.get('email'), UserType.OWNER)
        user_id = db.session.add(user)
        db.session.commit()
        return user_id
    except:
        return 404
