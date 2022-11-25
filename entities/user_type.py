from main import db
from entities.entity_dto import EntityDTO


class UserType(db.Model, EntityDTO):
    name = db.Column(db.String(10), primary_key=True, nullable=False)
    OWNER = 'OWNER'
    MANAGER = 'MANAGER'

    def __init__(self, name):
        self.name = name

def type_is_included(name, user_types):
    types_with_name = [t for t in user_types if t.name == name]
    if len(types_with_name) == 1:
        return types_with_name[0]
    return None

db.create_all()

types = UserType.query.all()
owner = type_is_included('OWNER', types)
manager = type_is_included('MANAGER', types)
if not owner:
    owner = UserType('OWNER')
    db.session.add(owner)
if not manager:
    manager = UserType('MANAGER')
    db.session.add(manager)
db.session.commit()

