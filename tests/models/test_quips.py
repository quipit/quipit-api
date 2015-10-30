from sqlalchemy.exc import IntegrityError

from quipit.app import db
from quipit.models import Quip, User, Circle

from tests.test_case import DBTestCase


class QuipTestCase(DBTestCase):
    def test_it_must_have_an_author(self):
        circle = Circle('SF Crew')
        quip = Quip("I'm not on trial here!", None, circle)

        db.session.add(quip)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_it_must_have_an_circle(self):
        user = User('Jonathan Como', 'jcomo')
        quip = Quip("I'm not on trial here!", user, None)

        db.session.add(quip)
        with self.assertRaises(IntegrityError):
            db.session.commit()
