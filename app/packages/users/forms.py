from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField,StringField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed
from .models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=30)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),EqualTo('password'),Length(min=8,max=30)])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('the Email already exist')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    last_name = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')

class EditUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('the Email already exist!')


class ContactForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('first_name', validators=[DataRequired()])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    submit = SubmitField('Submit')