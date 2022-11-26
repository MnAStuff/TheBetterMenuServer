from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/thebettermenu'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)

CORS(app)
db = SQLAlchemy(app)
