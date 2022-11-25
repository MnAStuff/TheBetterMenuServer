from main import db


class UserType(db.Model):
    name = db.Column(db.String(10), primary_key=True, nullable=False)
    OWNER = 'OWNER'
    MANAGER = 'MANAGER'

    def __init__(self, name):
        self.name = name


