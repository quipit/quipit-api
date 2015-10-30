from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from quipit.middleware import limit_size, accept_content
from quipit.utils import ellipsize

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Quip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(length=400))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('quips', lazy='dynamic'))


    def __init__(self, text, user=None):
        self.text = text
        self.user = user

    def _describe(self):
        return repr(ellipsize(self.text, length=40))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, name, username):
        self.name = name
        self.username = username


@app.route('/media/upload', methods=['POST'])
@accept_content(r'^image/(jpeg|jpg|png|gif)')
@limit_size(10 * 1024**2)
def upload():
    data = request.get_data()
    with open('data.jpg', 'wb') as f:
        f.write(data)

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
