from application import app, db
from flask import render_template, request, redirect, url_for
from application.tips.models import Tip

@app.route("/tips/new/")
def tips_form():
    return render_template("tips/new.html")

@app.route("/tips/", methods=["get"])
def list_tips():
    return render_template('tips/list.html', tips = Tip.query.all())

@app.route('/tips/<id>/like', methods=['POST'])
def like_tip(id):
    tip = Tip.query.get(id)
    tip.likes += 1
    db.session().commit()

    return redirect(url_for('list_tips'))

@app.route('/tips/<id>/unlike', methods=['POST'])
def unlike_tip(id): # tulee lisätä että yks user voi lisätä vain yhen
    tip = Tip.query.get(id)
    tip.dislikes += 1
    db.session().commit()

    return redirect(url_for('list_tips'))


@app.route("/tips/", methods=["POST"])
def tips_create():
    tip = Tip(request.form.get('name'))
    db.session().add(tip)
    db.session().commit()
  
    return redirect(url_for('list_tips'))
