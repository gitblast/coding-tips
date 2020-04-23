from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, validators

class TipForm(FlaskForm):
    content = TextAreaField("Your tip:", [validators.Length(min=8, max=160)])
    tag = StringField("Add tag:")
    add_tag = SubmitField('Add')

    link = StringField("Add link:")
    add_link = SubmitField('Add')

    tags = []
    links = []
 
    class Meta:
        csrf = False