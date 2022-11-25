import routing.registration
import routing.login
import routing.menu
from main import login_manager
from entities.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
