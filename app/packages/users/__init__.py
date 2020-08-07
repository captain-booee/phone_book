from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User, Contact
from app.init import db
from .forms import LoginForm, RegistrationForm
from flask_bcrypt import Bcrypt

bp = Blueprint("users", __name__, template_folder="templates/")
bcrypt = Bcrypt()


@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()

        #flash(f'Account created for {form.email.data}','success')
        return redirect(url_for('users.home'))
    return render_template('register.html',form = form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('users.home'))
    return render_template('login.html', form=form)