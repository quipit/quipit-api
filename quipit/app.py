from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from quipit.middleware import limit_size, accept_content
from quipit.utils import ellipsize

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/media/upload', methods=['POST'])
@accept_content(r'^image/(jpeg|jpg|png|gif)')
@limit_size(10 * 1024 ** 2)
def upload():
    data = request.get_data()
    with open('data.jpg', 'wb') as f:
        f.write(data)

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
