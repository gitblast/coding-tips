from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.tips.models import Tip
from application.tips.forms import TipForm

@app.route("/tips/new/")
@login_required
def tips_form():
    return render_template("tips/new.html", form = TipForm())

@app.route("/tips/", methods=["get"])
def list_tips():
    return render_template('tips/list.html', tips = Tip.query.all())

@app.route('/tips/<id>/like', methods=['POST'])
@login_required
def like_tip(id):
    tip = Tip.query.get(id)
    tip.likes += 1
    db.session().commit()

    return redirect(url_for('list_tips'))

@app.route('/tips/<id>/unlike', methods=['POST'])
@login_required
def unlike_tip(id): # tulee lisätä että yks user voi lisätä vain yhen
    tip = Tip.query.get(id)
    tip.dislikes += 1
    db.session().commit()

    return redirect(url_for('list_tips'))


@app.route("/tips/", methods=["POST"])
@login_required
def tips_create():
    form = TipForm(request.form)

    if not form.validate():
        return render_template("tips/new.html", form = form)

    tip = Tip(form.content.data)

    db.session().add(tip)
    db.session().commit()
  
    return redirect(url_for('list_tips'))
