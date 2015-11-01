from tests.test_case import APITestCase

from quipit.db import db
from quipit.models import User


class CreateQuipTestCase(APITestCase):
    def test_it_creates_quip_with_no_circles(self):
        # NOTE: to send multiple values for the same key (ie. circle=1&circle=2)
        # use {'circle': [1, 2]} and the client will transform that automatically
        text = "I'm not on trial here!"
        response = self.client.post('/quips', data={'text': text})

        # TODO: this will change when we have real auth
        user = User.query.first()
        created_quip = user.quips.first()

        self.assertEqual(1, user.quips.count())
        self.assertEqual(text, created_quip.text)
        self.assertEqual([], created_quip.circles.all())
