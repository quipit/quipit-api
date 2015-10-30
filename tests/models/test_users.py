from unittest import TestCase

from quipit.app import db, Quip, User


class UserTestCase(TestCase):
    def setUp(self):
        super(UserTestCase, self).setUp()
        db.create_all()
        self.user = User('Jonathan Como', 'jcomo')

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_can_retrieve_quips(self):
        user = User('Jonathan Como', 'jcomo')
        user_quip = Quip('This is some thangs', user)
        other_user_quip = Quip('This is none thangs')

        db.session.add(user_quip)
        db.session.add(other_user_quip)
        db.session.commit()

        self.assertEqual([user_quip], user.quips.all())

