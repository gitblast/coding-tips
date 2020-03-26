from application import db

#TODO: lisää date modified

class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    add_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    content = db.Column(db.String(160), nullable=False)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, content):
        self.content = content
