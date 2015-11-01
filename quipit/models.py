from quipit.db import db
from quipit.utils import ellipsize


users_circles = db.Table('users_circles',
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                         db.Column('circle_id', db.Integer, db.ForeignKey('circle.id')))


quips_circles = db.Table('quips_circles',
                         db.Column('quip_id', db.Integer, db.ForeignKey('quip.id')),
                         db.Column('circle_id', db.Integer, db.ForeignKey('circle.id')))


class Quip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(length=400))

    circles = db.relationship('Circle',
                              secondary=quips_circles,
                              lazy='dynamic',
                              backref=db.backref('quips', lazy='dynamic'))

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User',
                             backref=db.backref('quips', lazy='dynamic'),
                             foreign_keys=[author_id])

    source_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    source = db.relationship('User',
                             backref=db.backref('quotes', lazy='dynamic'),
                             foreign_keys=[source_id])

    def __init__(self, text, author, circle=None, source=None):
        self.text = text
        self.author = author
        self.circle = circle
        self.source = source

    def __repr__(self):
        quip_text = repr(ellipsize(self.text))
        return '<Quip {}>'.format(quip_text)

    def add_to_circle(self, circle):
        self.circles.append(circle)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, name, username):
        self.name = name
        self.username = username

    def __repr__(self):
        return '<User {} ({})>'.format(repr(self.name), self.username)

    @classmethod
    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()


class Circle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    members = db.relationship('User',
                              secondary=users_circles,
                              lazy='dynamic',
                              backref=db.backref('circles', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    @property
    def quip_count(self):
        return self.quips.count()

    @property
    def member_count(self):
        return self.members.count()

    def add_member(self, user):
        self.members.append(user)

    def add_quip(self, quip):
        self.quips.append(quip)
