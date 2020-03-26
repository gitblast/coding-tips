from flask_wtf import FlaskForm
from wtforms import TextAreaField,validators

class TipForm(FlaskForm):
    content = TextAreaField("Your tip:", [validators.Length(min=8, max=160)])
 
    class Meta:
        csrf = False