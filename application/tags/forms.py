from wtforms import StringField, validators
from flask_wtf import FlaskForm

class TagForm(FlaskForm):
    tag = StringField('Tag:', [validators.Length(min=1, max=20)])

    class Meta:
        csrf = False