from flask import render_template
from application import app

from application.tips.models import Tip
from application.tags.models import Tag
from application.users.models import User

@app.route("/")
def index():
    return render_template("index.html", tips = Tip.count(), tags = Tag.count(), users = User.count())