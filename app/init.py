from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


login_manager = LoginManager()
login_manager.login_view = 'users.login'
#login_manager.login_message_category = 'class name'

db = SQLAlchemy()
bcrypt = Bcrypt()