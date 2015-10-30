from quipit.app import db, Quip, User

from tests.test_case import DBTestCase


class UserTestCase(DBTestCase):
    def test_user_can_retrieve_quips(self):
        user = User('Jonathan Como', 'jcomo')
        user_quip = Quip('This is some thangs', user)

        other_user = User('Peter Como', 'pcomo')
        other_user_quip = Quip('This is none thangs', other_user)

        db.session.add(user_quip)
        db.session.add(other_user_quip)
        db.session.commit()

        self.assertEqual([user_quip], user.quips.all())
