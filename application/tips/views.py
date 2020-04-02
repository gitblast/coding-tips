from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db

from application.tips.models import Tip
from application.tips.forms import TipForm

from application.tags.models import Tag

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
    tip = Tip.query.get(id)
    if tip.account_id != current_user.id:
        print('Error: cannot delete tips added by others')
        return redirect(request.referrer)
    db.session().delete(tip)
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

@app.route('/tips/<id>/update', methods=['GET', 'POST'])
@login_required
def update_tip(id):
    tip = Tip.query.get(id)

    if (request.method == 'GET'):
        return render_template('tips/update.html', tip = tip, form = TipForm(), text = tip.content)

    form = TipForm(request.form)
    
    if not form.validate():
        return render_template('tips/update.html', tip = tip, form = form, text = form.content.data)

    if tip.account_id != current_user.id:
        print('Error: cannot update tips added by others')
        return redirect(request.referrer)
    tip.content = form.content.data
    db.session().commit()

    print('tip updated')

    return redirect(url_for('user_tips'))


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

    if (form.add_tag.data):
        if (len(form.tag.data) < 1 or len(form.tag.data) > 20):
            return render_template("tips/new.html", form = form, tagError = 'Tag must be between 1 and 20 characters long.')
        form.tags.append(form.tag.data)
        return render_template("tips/new.html", form = form)

    if not form.validate():
        return render_template("tips/new.html", form = form)

    tip = Tip(form.content.data)
    tip.account_id = current_user.id

    # lisätään tietokantaan ne tagit, joita ei sieltä jo löydy, ja lisätään tagit tipin tageihin
    for tag in form.tags:
        dbTag = Tag.query.filter_by(content=tag).first()
        if not dbTag:
            t = Tag(tag)
            t.account_id = current_user.id
            test = db.session().add(t)
            dbTag = Tag.query.filter_by(content=tag).first()
        tip.tags.append(dbTag)

    db.session().add(tip)
    db.session().commit()
  
    return redirect(url_for('list_tips'))
