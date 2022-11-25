from main import db


class OrderState(db.Model):
    name = db.Column(db.String(10), primary_key=True, nullable=False)
    DONE = 'DONE'
    PENDING = 'PENDING'
    NEW = 'NEW'
    CLOSED = 'CLOSED'

    def __init__(self, name):
        self.name = name


