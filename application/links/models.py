from application import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(60), nullable=False)

    tip_id = db.Column(db.Integer, db.ForeignKey('tip.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, url):
        self.url = url