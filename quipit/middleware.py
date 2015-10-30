import re
from functools import wraps

from flask import request
from werkzeug import exceptions


def authenticate(f):
    from quipit.app import db
    from quipit.models import User

    @wraps(f)
    def _authenticate(*args, **kwargs):
        # TODO: do real authentication (none of these thangs)
        user = User.find_by_username('jcomo')
        if not user:
            user = User('Jonathan Como', 'jcomo')
            db.session.add(user)
            db.session.commit()
            print '[DEBUG] Created user jcomo'

        kwargs['user'] = user
        return f(*args, **kwargs)
    return _authenticate


def limit_size(size):
    def _limit_size(f):
        @wraps(f)
        def __limit_size(*args, **kwargs):
            if request.content_length > size:
                raise exceptions.RequestEntityTooLarge

            return f(*args, **kwargs)
        return __limit_size
    return _limit_size


def accept_content(content_regex):
    def _accept_content(f):
        @wraps(f)
        def __accept_content(*args, **kwargs):
            if not re.match(content_regex, request.content_type):
                raise exceptions.UnsupportedMediaType

            return f(*args, **kwargs)
        return __accept_content
    return _accept_content
