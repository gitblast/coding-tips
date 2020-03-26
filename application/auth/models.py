from application import db

class User(db.Model): #TODO: hashaa passwordit ja lisää validointeja
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

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True