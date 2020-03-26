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
    password = PasswordField("Password", [validators.InputRequired()])
    passwordRepeat = PasswordField("Repeat password", [validators.InputRequired(), validators.InputRequired()])
    email = StringField("Email address", [validators.Email('Valid email address required')])

    class Meta:
        csrf = False