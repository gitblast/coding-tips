from application import db

from sqlalchemy.sql import text

tags = db.Table('tip_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('tip_id', db.Integer, db.ForeignKey('tip.id'), primary_key=True)
)

class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    add_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
        onupdate=db.func.current_timestamp())

    content = db.Column(db.String(160), nullable=False)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    links = db.relationship('Link', backref='tip', lazy=True)

    tags = db.relationship(
        'Tag',
        secondary=tags,
        lazy='subquery',
        backref=db.backref('tips', lazy=True)
    )

    @staticmethod
    def count():
        stmt = text("SELECT COUNT(*) from tip")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

        return None


    def __init__(self, content):
        self.content = content
