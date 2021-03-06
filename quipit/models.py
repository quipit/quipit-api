from quipit.app import db
from quipit.utils import ellipsize


class Quip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(length=400))

    circle_id = db.Column(db.Integer, db.ForeignKey('circle.id'), nullable=False)
    circle = db.relationship('Circle',
                             backref=db.backref('quips', lazy='dynamic'))

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User',
                             backref=db.backref('quips', lazy='dynamic'),
                             foreign_keys=[author_id])

    source_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    source = db.relationship('User',
                             backref=db.backref('quotes', lazy='dynamic'),
                             foreign_keys=[source_id])

    def __init__(self, text, author, circle):
        self.text = text
        self.author = author
        self.circle = circle

    def __repr__(self):
        quip_text = repr(ellipsize(self.text))
        return '<Quip {}>'.format(quip_text)


users_circles = db.Table('users_circles',
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                         db.Column('circle_id', db.Integer, db.ForeignKey('circle.id')))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, name, username):
        self.name = name
        self.username = username

    def __repr__(self):
        return '<User {} ({})>'.format(repr(self.name), self.username)


class Circle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    members = db.relationship('User',
                              secondary=users_circles,
                              lazy='dynamic',
                              backref=db.backref('circles', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def add_member(self, user):
        self.members.append(user)
