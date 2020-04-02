from application import app

from application.auth.models import User
from flask import render_template

@app.route("/users/")
def list_users():
    users = User.query.all()
    for user in users:
        user.likes = user.getLikes(user.id)
        user.dislikes = user.getDislikes(user.id)
    return render_template('users/list.html', users = users)