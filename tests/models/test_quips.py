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
