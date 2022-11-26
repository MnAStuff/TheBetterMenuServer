import routing.registration
import routing.login
import routing.menu
import routing.dish
import routing.order
import routing.restaurant
from main import login_manager
from entities.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

