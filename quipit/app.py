from flask import Flask, request

from quipit.api import api
from quipit.db import db
from quipit.middleware import limit_size, accept_content
from quipit.resources import QuipsResource
from quipit.utils import ellipsize

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
api.init_app(app)


@app.route('/media/upload', methods=['POST'])
@accept_content(r'^image/(jpeg|jpg|png|gif)')
@limit_size(10 * 1024**2)
def upload():
    data = request.get_data()
    with open('data.jpg', 'wb') as f:
        f.write(data)

    return 'OK'
