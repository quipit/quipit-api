from unittest import TestCase
from mock import patch

from werkzeug import exceptions

from quipit.middleware import limit_size


class MaxContentLengthTestCase(TestCase):

    def test_it_rejects_the_request_if_content_length_too_long(self):

        @limit_size(100)
        def route():
            return 'OK'

        with patch('quipit.middleware.request') as req:
            req.content_length = 101
            with self.assertRaises(exceptions.RequestEntityTooLarge):
                route()

    def test_it_continues_with_request_if_content_length_below_threshold(self):

        @limit_size(100)
        def route():
            return 'OK'

        with patch('quipit.middleware.request') as req:
            req.content_length = 99
            self.assertEqual('OK', route())
