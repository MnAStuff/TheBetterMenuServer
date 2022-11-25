from entities.user_type import UserType
from dataclasses import dataclass
from main import db
from entities.entity_dto import EntityDTO

@dataclass
class User(db.Model, EntityDTO):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(10), db.ForeignKey('user_type.name'), nullable=False)

    def __init__(self, login, password, email, type):
        self.login = login
        self.password = password
        self.email = email
        self.type = type


# db.create_all()
# db.session.add(User('login1', 'password1', 'email@email.com', 'OWNER'))
# db.session.commit()
