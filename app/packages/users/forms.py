from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField,StringField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from .models import User

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