from unittest import TestCase
from mock import patch

from werkzeug import exceptions

from quipit.middleware import accept_content


class AllowedContentTypesTestCase(TestCase):

    def test_it_rejects_the_request_if_content_type_is_not_a_match(self):

        @accept_content('^image/jpeg')
        def route():
            return 'OK'

        with patch('quipit.middleware.request') as req:
            req.content_type = 'image/png'
            with self.assertRaises(exceptions.UnsupportedMediaType):
                route()

    def test_it_continues_with_request_if_content_type_is_a_match(self):

        @accept_content('^image/*')
        def route():
            return 'OK'

        with patch('quipit.middleware.request') as req:
            req.content_type = 'image/jpeg'
            self.assertEqual('OK', route())
