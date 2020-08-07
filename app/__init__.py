from flask import Flask,render_template,flash,redirect,url_for
from app.init import db
from app.packages import users
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app, )
app.register_blueprint(users.bp)

# need to :
#from app import db
#db.create_all()

#from app import User,Contact
#User.query.all()
#db.session.add(User(email='',...))
#db.session.commit()

# user_1 = user.query.filter_by(email='').all()
# a = user_1.id
# contact_1 = Contact(......, user_id=a)
# contact_1.user_id