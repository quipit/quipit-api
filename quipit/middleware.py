from werkzeug import exceptions


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
