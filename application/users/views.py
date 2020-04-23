from application import app

from application.users.models import User
from flask import render_template

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