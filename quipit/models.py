from quipit.app import db


class Quip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(length=400))

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User',
                             backref=db.backref('quips', lazy='dynamic'),
                             foreign_keys=[author_id])

    source_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    source = db.relationship('User',
                             backref=db.backref('quotes', lazy='dynamic'),
                             foreign_keys=[source_id])

    def __init__(self, text, author=None):
        self.text = text
        self.author = author

    def _describe(self):
        return repr(ellipsize(self.text, length=40))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, name, username):
        self.name = name
        self.username = username
