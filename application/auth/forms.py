from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

# TODO: unique user validaatio!

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.Length(min=8, message='Password must be at least 8 characters')])
    passwordRepeat = PasswordField("Repeat password", [validators.EqualTo('password', message="Passwords don't match")])
    email = StringField("Email address", [validators.Email('Valid email address required')])

    class Meta:
        csrf = False