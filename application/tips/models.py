from application import db

tags = db.Table('tip_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('tip_id', db.Integer, db.ForeignKey('tip.id'), primary_key=True)
)

class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    add_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
        onupdate=db.func.current_timestamp())

    content = db.Column(db.String(160), nullable=False)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    tags = db.relationship(
        'Tag',
        secondary=tags,
        lazy='subquery',
        backref=db.backref('tips', lazy=True)
    )

    def __init__(self, content):
        self.content = content
