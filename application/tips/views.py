from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db

from application.tips.models import Tip
from application.tips.forms import TipForm

from application.tags.models import Tag
from application.users.models import User
from application.links.models import Link

@app.route("/tips/new/")
@login_required
def tips_form():
    return render_template("tips/new.html", form = TipForm(), text = None)

@app.route("/tips/", methods=["get"])
def list_tips():
    tips = Tip.query.all()
    tags = Tag.query.all()
    users = User.query.all()

    for u in users: 
        u.strid = str(u.id)

    sort = request.args.get('sort')
    filt = request.args.get('filter')
    user = request.args.get('user')

    if user:
        tips = list(filter(lambda tip: tip.account_id == int(user), tips))

    if sort == 'likes':
        print('sorting by likes')
        tips.sort(key=lambda tip: tip.likes, reverse=True)
    elif sort == 'date':
        print('sorting by date')
        tips.sort(key=lambda tip: tip.add_date)
    elif sort == "dislikes":
        print('sorting by dislikes')
        tips.sort(key=lambda tip: tip.dislikes, reverse=True)

    if filt:
        print('filter:', filt)
        tips = [tip for tip in tips if filt in [tag.content for tag in tip.tags]]

    return render_template('tips/list.html', tips = tips, tags = tags, sort = sort, filt = filt, user = user, users = users)

@app.route("/tips/<id>")
def show_tip(id):
    return render_template('tips/list.html', tips = Tip.query.filter_by(id=id))

@app.route("/tips/<id>/delete", methods=['POST'])
@login_required
def delete_tip(id):
    tip = Tip.query.get(id)
    if tip.account_id != current_user.id and not current_user.isAdmin:
        print('Error: cannot delete tips added by others unless admin')
        return redirect(request.referrer)
    db.session.delete(tip)
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

@app.route('/tips/<id>/update', methods=["GET"])
@login_required
def update_tip(id):
    tip = Tip.query.get(id)
    form = TipForm()
    form.tags = list(map(lambda tag: tag.content, tip.tags))
    form.links = list(map(lambda link: link.url, tip.links))
    return render_template('tips/update.html', tip = tip, form = form, text = tip.content)

@app.route('/tips/<id>/update/<what>', methods=["POST"])
@login_required
def update_tip_property(id, what):
    tip = Tip.query.get(id)
    form = TipForm(request.form)
    
    if what == 'text':
        tip.content = form.content.data
        db.session().commit()
        updated = Tip.query.get(id)
        form.tags = list(map(lambda tag: tag.content, tip.tags))
        form.links = list(map(lambda link: link.url, tip.links))
        return render_template('tips/update.html', tip = updated, form = form, text = updated.content, text_msg = "Tip content updated succesfully")

    if what == 'links':
        for tag in tip.tags:
            if tag.content not in form.tags:
                form.tags.append(tag.content)
        for link in tip.links:
            if link.url not in form.links:
                form.links.append(link.url)
        if (form.add_link.data):
            data = form.link.data
            if not (data.startswith("http://") or data.startswith("https://") or data.startswith("www.")):
                return render_template("tips/update.html", tip = tip, form = form, text = tip.content, linkError = "A valid URL is required.")
            if data in form.links:
                return render_template("tips/update.html", tip = tip, form = form, text = tip.content, linkError = "No duplicate links allowed.")
            form.links.append(form.link.data)
            form.link.data = ''
            return render_template("tips/update.html", form = form, tip = tip, text = tip.content)

        for link in form.links:
            l = Link(link)
            l.account_id = current_user.id
            l.tip_id = tip.id
            db.session().add(l)

        db.session().commit()

        updated = Tip.query.get(id)

        return render_template('tips/update.html', tip = updated, form = form, text = tip.content, link_msg = "Links updated successfully")

    if what == 'tags':
        for link in tip.links:
            if link.url not in form.links:
                form.links.append(link.url)
        for tag in tip.tags:
            if tag.content not in form.tags:
                form.tags.append(tag.content)
        if (form.add_tag.data):
            if (len(form.tag.data) < 1 or len(form.tag.data) > 20):
                return render_template("tips/update.html", tip = tip, text = tip.content, form = form, tagError = 'Tag must be between 1 and 20 characters long.')
            if tag in form.tags:
                return render_template("tips/update.html", tip = tip, text = tip.content, form = form, tagError = 'No duplicate tags allowed')
            
            form.tags.append(form.tag.data)
            form.tag.data = ''
            return render_template('tips/update.html', tip = tip, form = form, text = tip.content)

        for tag in form.tags:
            if tag not in list(map(lambda t: t.content, tip.tags)):
                dbTag = Tag.query.filter_by(content=tag).first()
                if not dbTag:
                    t = Tag(tag)
                    t.account_id = current_user.id
                    test = db.session().add(t)
                    dbTag = Tag.query.filter_by(content=tag).first()
                tip.tags.append(dbTag)

        db.session().add(tip)
        db.session().commit()

        updated = Tip.query.get(id)
            
        return render_template('tips/update.html', tip = updated, form = form, text = updated.content, tag_msg = "Tags updated succesfully")


@app.route('/tips/<id>/unlike', methods=['POST'])
@login_required
def unlike_tip(id):
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
        form.tag.data = ''
        return render_template("tips/new.html", form = form)

    if (form.add_link.data):
        data = form.link.data
        if not (data.startswith("http://") or data.startswith("https://") or data.startswith("www.")):
            return render_template("tips/new.html", form = form, linkError = "A valid URL is required.")
        form.links.append(form.link.data)
        form.link.data = ''
        return render_template("tips/new.html", form = form)

    if not form.validate():
        return render_template("tips/new.html", form = form)

    tip = Tip(form.content.data)
    tip.account_id = current_user.id

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
    
    dbTip = Tip.query.filter_by(content=tip.content, account_id=current_user.id).first()

    for link in form.links:
        l = Link(link)
        l.account_id = current_user.id
        l.tip_id = dbTip.id
        db.session().add(l)

    db.session().commit()

    TipForm.tags = []
    TipForm.links = []
  
    return redirect(url_for('list_tips'))
