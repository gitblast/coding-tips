from application import db

from sqlalchemy.sql import text

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(20), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    @staticmethod
    def count():
        stmt = text("SELECT COUNT(*) FROM tag")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

        return None


    def __init__(self, content):
        self.content = content