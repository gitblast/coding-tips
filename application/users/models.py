from application import db

from sqlalchemy.sql import text

class User(db.Model): #TODO: hashaa passwordit ja lisää validointeja, ja refaktoroi users kansioon!
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    join_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password= db.Column(db.String(160), nullable=False)

    tips = db.relationship('Tip', backref='account', lazy=True)

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def userWithMostLikes():
        return None

    @staticmethod
    def getLikes(userId):
        stmt = text("SELECT SUM(likes) FROM tip WHERE account_id = :id").params(id=userId)
        res = db.engine.execute(stmt)

        result = 0

        for row in res:
            if row[0]:
                result = row[0]

        return result

    @staticmethod
    def getDislikes(userId):
        stmt = text("SELECT SUM(dislikes) FROM tip WHERE account_id = :id").params(id=userId)
        res = db.engine.execute(stmt)

        result = 0

        for row in res:
            if row[0]:
                result = row[0]

        return result

    @staticmethod
    def getMostLiked(userId):
        stmt = text("SELECT id, content, likes FROM tip WHERE account_id = :id ORDER BY likes DESC LIMIT 1").params(id=userId)
        res = db.engine.execute(stmt)

        result = None

        for row in res:
            if (row[0] and row[1] and row[2]):
                result = (row[0], row[1], row[2])

        return result

    @staticmethod
    def count():
        stmt = text("SELECT COUNT(*) FROM account")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

        return None

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True