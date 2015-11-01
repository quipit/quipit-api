from sqlalchemy.exc import IntegrityError

from quipit.app import db
from quipit.models import Quip, User, Circle

from tests.test_case import DBTestCase


class QuipTestCase(DBTestCase):
    def test_it_must_have_an_author(self):
        quip = Quip("I'm not on trial here!", None)

        db.session.add(quip)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_it_can_be_added_to_many_circles(self):
        user = User('Jonathan Como', 'jcomo')
        quip = Quip("I'm not on trial here!", user)

        circle = Circle('SF Crew')
        other_circle = Circle('College Buds')

        quip.add_to_circle(circle)
        quip.add_to_circle(other_circle)

        db.session.add(quip)
        db.session.commit()

        self.assertEqual(sorted([circle, other_circle]), sorted(quip.circles.all()))
