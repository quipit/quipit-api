import re
from functools import wraps

from flask import Flask, request, abort
from werkzeug import exceptions

app = Flask(__name__)


def limit_size(size):
    def _limit_size(f):
        def __limit_size(*args, **kwargs):
            if request.content_length > size:
                raise exceptions.RequestEntityTooLarge

            return f(*args, **kwargs)
        return __limit_size
    return _limit_size


def accept_content(content_regex):
    def _accept_content(f):
        def __accept_content(*args, **kwargs):
            if not re.match(content_regex, request.content_type):
                abort(415)

            return f(*args, **kwargs)
        return __accept_content
    return _accept_content


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
