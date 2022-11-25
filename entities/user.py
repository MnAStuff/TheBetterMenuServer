from dataclasses import dataclass
from main import db
from flask_login import UserMixin


@dataclass
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    type = db.Column(db.String(10), db.ForeignKey('user_type.name'), nullable=False)

    restaurants = db.relationship('Restaurant', backref='user', lazy=False)

    def __init__(self, login, password, email, type):
        self.login = login
        self.password = password
        self.email = email
        self.type = type