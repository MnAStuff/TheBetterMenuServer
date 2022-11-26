from entities.order_state import OrderState
from entities.user_type import UserType
from entities.user import User
from entities.order import Order
from entities.ordered_dish import OrderedDish
from entities.restaurant import Restaurant
from entities.menu import Menu
from entities.dish_type import DishType
from entities.dish import Dish
from main import db
from werkzeug.security import generate_password_hash

# db.drop_all()
db.create_all()


def type_is_included(name, user_types):
    types_with_name = [t for t in user_types if t.name == name]
    if len(types_with_name) == 1:
        return types_with_name[0]
    return None


types = UserType.query.all()
owner = type_is_included(UserType.OWNER, types)
manager = type_is_included(UserType.MANAGER, types)
if not owner:
    owner = UserType(UserType.OWNER)
    db.session.add(owner)
if not manager:
    manager = UserType(UserType.MANAGER)
    db.session.add(manager)
db.session.commit()

types = OrderState.query.all()
new = type_is_included(OrderState.NEW, types)
pending = type_is_included(OrderState.PENDING, types)
closed = type_is_included(OrderState.CLOSED, types)
done = type_is_included(OrderState.DONE, types)
if not new:
    new = OrderState(OrderState.NEW)
    db.session.add(new)
if not pending:
    pending = OrderState(OrderState.PENDING)
    db.session.add(pending)
if not closed:
    closed = OrderState(OrderState.CLOSED)
    db.session.add(closed)
if not done:
    done = OrderState(OrderState.DONE)
    db.session.add(done)
db.session.commit()

types = DishType.query.all()
meat = type_is_included('Meat', types)
fish = type_is_included('Fish', types)
drinks = type_is_included('Drinks', types)

if not meat:
    meat = DishType('Meat')
    db.session.add(meat)
if not fish:
    fish = DishType('Fish')
    db.session.add(fish)
if not drinks:
    drinks = DishType('Drinks')
    db.session.add(drinks)
db.session.commit()

# init mocks

# user = User('login', generate_password_hash('password'), 'rgwergwergwre', UserType.OWNER)
# db.session.add(user)
# db.session.commit()
#
# restaurant = Restaurant('restaurant_name', 'restaurant_address', 'restaurant_description', user)
# db.session.add(restaurant)
# db.session.commit()
#
# menu = Menu(restaurant)
# menu1 = Menu(restaurant)
# db.session.add(menu)
# db.session.add(menu1)
# db.session.commit()
#
# dish1 = Dish('name11', 'Meat', 'description11', menu, 100, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish2 = Dish('name12', 'Meat', 'description12', menu, 100, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish3 = Dish('name13', 'Meat', 'description13', menu, 100, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
#
# dish4 = Dish('name21', 'Fish', 'description21', menu, 150, 'RUB',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish5 = Dish('name22', 'Fish', 'description22', menu, 150, 'RUB',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish6 = Dish('name23', 'Fish', 'description23', menu, 150, 'RUB',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
#
# dish7 = Dish('name31', 'Drinks', 'description31', menu, 200, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish8 = Dish('name32', 'Drinks', 'description32', menu, 200, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish9 = Dish('name33', 'Drinks', 'description33', menu, 200, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
#
#
# dish10 = Dish('name41', 'Drinks', 'description333333331', menu1, 2300, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish11 = Dish('name42', 'Fish', 'description3332', menu1, 2010, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
# dish12 = Dish('name43', 'Drinks', 'description3333', menu1, 400, 'USD',
#              'будет типа ссылка на закгрузку изображения с серввера это изи отвечаю бля буду', True)
#
# db.session.add_all([dish1, dish2, dish3, dish4, dish5, dish6, dish7, dish8, dish9, dish10, dish11, dish11])
#
# db.session.commit()
