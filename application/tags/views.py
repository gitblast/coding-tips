from application import app, db

from application.tags.models import Tag
from application.tags.forms import TagForm

from flask import redirect, request, render_template
from flask_login import current_user, login_required

@app.route('/tags/', methods=['GET'])
def list_tags():
    return render_template('tags/list.html', form = TagForm(), tags = Tag.query.all())

@app.route('/tags/', methods=['POST'])
@login_required
def add_tag():
    form = TagForm(request.form)

    if not form.validate():
        return render_template('tags/list.html', form = form)

    tag = Tag(form.tag.data)
    tag.account_id = current_user.id

    db.session().add(tag)
    db.session().commit()

    return redirect(request.referrer)

@app.route('/tags/<id>', methods=['POST'])
@login_required
def delete_tag(id):
    tag = Tag.query.get(id)

    if tag.account_id != current_user.id:
        print('Error: cannot delete tags added by others')
        return redirect(request.referrer)
    db.session().delete(tag)
    db.session().commit()
    return redirect(request.referrer)
