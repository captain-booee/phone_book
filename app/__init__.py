from flask import Flask,render_template,flash,redirect,url_for
from app.user.forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True, nullable=False)
        image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
        password = db.Column(db.String(60), nullable=False)

        def __repr__(self):
            return f"User('{self.email}','{self.image_file}')"

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/register', methods=['GET','POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'Account created for {form.email.data}','success')
            return redirect(url_for('home'))
        return render_template('register.html',form = form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            #flash(f'Account created for {form.email.data}', 'success')
            return redirect(url_for('home'))
        return render_template('login.html', form=form)


    return app