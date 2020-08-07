from flask import Flask,render_template,flash,redirect,url_for
from app.init import db
from app.packages import users


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app, )
    app.register_blueprint(users.bp)
    return app

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