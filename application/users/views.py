from application import app, db

from application.users.models import User
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

@app.route("/users/")
def list_users():
    users = User.query.all()
    mostTips = None
    mostLikes = None
    mostDislikes = None

    for user in users:
        if not mostTips or len(user.tips) > len(mostTips.tips):
            mostTips = user

        user.likes = user.getLikes(user.id)
        if not mostLikes or user.likes > mostLikes.likes:
            mostLikes = user
        user.dislikes = user.getDislikes(user.id)
        if not mostDislikes or user.dislikes > mostDislikes.dislikes:
            mostDislikes = user
        user.mostLiked = user.getMostLiked(user.id)
    return render_template('users/list.html', users = users, mostTips = mostTips, mostLikes = mostLikes, mostDislikes = mostDislikes)


@app.route("/users/<id>/upgrade", methods=['POST'])
@login_required
def make_admin(id):
    if not current_user.isAdmin:
        return redirect(request.referrer)
    
    user = User.query.get(id)
    user.isAdmin = True

    db.session().commit()

    return redirect(request.referrer)