import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import User, Contact
from app.init import db, bcrypt
from .forms import LoginForm, RegistrationForm, SearchForm, EditUserForm
from flask_login import login_user, current_user, logout_user, login_required


bp = Blueprint("users", __name__, template_folder="templates/")


@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.email.data}','success')
        return redirect(url_for('users.home'))
    return render_template('register.html', form = form, title='Register')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.home'))
        else:
            flash(f'login failed. please check email and password  {form.email.data}', 'danger')
        #return redirect(url_for('users.profile'))

    return render_template('login.html', form=form, title='Login')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.home'))

@bp.route('/profile')
@login_required
def profile():
    form = SearchForm()
    #if form.validate_on_submit():

    image_src = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='Profile', form=form, image_src=image_src)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(bp.root_path, '../../static/profile_pics',picture_fn)
    output_size = (100,100)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn

@bp.route('/edit_user', methods=['GET', 'POST'])
@login_required
def edit_user():
    form = EditUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated.')
        return redirect(url_for('users.edit_user'))
    elif request.method == 'GET':
        form.email.data = current_user.email
    image_src = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('edit_user.html', title='Profile Edit', form=form, image_src=image_src)