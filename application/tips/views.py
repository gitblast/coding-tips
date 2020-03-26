from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

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

@app.route("/tips/my")
@login_required
def user_tips():
    return render_template('tips/list.html', tips = Tip.query.filter_by(account_id=current_user.id))

@app.route("/tips/<id>") #TODO: tee oma tarkempi näkymä
def show_tip(id):
    return render_template('tips/list.html', tips = Tip.query.filter_by(id=id))

@app.route("/tips/<id>/delete", methods=['POST'])
@login_required
def delete_tip(id):
    Tip.query.filter_by(id=id).delete()
    db.session().commit()
    return redirect(request.referrer)

@app.route('/tips/<id>/like', methods=['POST'])
@login_required
def like_tip(id):
    tip = Tip.query.get(id)
    if (tip.account_id == current_user.id):
        print("Error: can't like/unlike your own tip")
        return redirect(request.referrer)

    tip.likes += 1
    db.session().commit()

    return redirect(request.referrer)

@app.route('/tips/<id>/unlike', methods=['POST'])
@login_required
def unlike_tip(id): # tulee lisätä että yks user voi lisätä vain yhen
    tip = Tip.query.get(id)
    if (tip.account_id == current_user.id):
        print("Error: can't like/unlike your own tip")
        return redirect(request.referrer)

    tip.dislikes += 1
    db.session().commit()

    return redirect(request.referrer)


@app.route("/tips/", methods=["POST"])
@login_required
def tips_create():
    form = TipForm(request.form)

    if not form.validate():
        return render_template("tips/new.html", form = form)

    tip = Tip(form.content.data)
    tip.account_id = current_user.id

    db.session().add(tip)
    db.session().commit()
  
    return redirect(url_for('list_tips'))
