from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SelectMultipleField, SubmitField, validators

class TipForm(FlaskForm):
    content = TextAreaField("Your tip:", [validators.Length(min=8, max=160)])
    #tags = SelectMultipleField('Tags:', choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])
    tag = StringField("Add tag:")
    add_tag = SubmitField('Add')

    tags = []
 
    class Meta:
        csrf = False