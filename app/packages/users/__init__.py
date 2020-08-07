from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User, Contact
from app.init import db
from .forms import LoginForm, RegistrationForm

from app import bcrypt
from flask_login import login_user

bp = Blueprint("users", __name__, template_folder="templates/")


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
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)

        #flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('users.home'))
    return render_template('login.html', form=form)