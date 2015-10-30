from quipit.app import db, Quip, User

from tests.test_case import DBTestCase


class QuipTestCase(DBTestCase):
    def setUp(self):
        super(QuipTestCase, self).setUp()
        self.user = User('Jonathan Como', 'jcomo')

    def test_it_can_have_an_author(self):
        quip = Quip("I'm not on trial here!", self.user)

        db.session.add(quip)
        db.session.commit()

        self.assertIsNotNone(self.user.id)

    def test_it_does_not_need_an_author(self):
        quip = Quip("Four score and seven years ago...")

        db.session.add(quip)
        db.session.commit()
