from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Invalid username or password")

    login_user(user)
    print('Login succesful for username:', user.username)
    return redirect(url_for('index'))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register/", methods = ['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        print('add new user')
        return render_template("auth/register.html", form = RegisterForm())

    form = RegisterForm(request.form)

    # TODO: passwordien tulee olla samat molemmissa kentissä
    if not form.validate():
        print('validation error adding user')
        return render_template('auth/register.html', form = form, error = 'Sign up failed')

    # TODO: passwordhash
    user = User(form.username.data, form.password.data, form.email.data)
    
    db.session().add(user)
    db.session().commit()

    return redirect(url_for('index'))