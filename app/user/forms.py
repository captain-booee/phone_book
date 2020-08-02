from flask_wtf import FlaskForm
from wtforms import SelectField,PasswordField, SubmitField, BooleanField,StringField
from wtforms.validators import DataRequired, Length, EqualTo, Email



class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=30)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),EqualTo('password'),Length(min=8,max=30)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')