from quipit.app import db
from quipit.models import Quip, User, Circle

from tests.test_case import DBTestCase


class UserTestCase(DBTestCase):
    def test_users_can_be_found_by_username(self):
        user = User('Jonathan Como', 'jcomo')
        other_user = User('Peter Como', 'pcomo')

        db.session.add(user)
        db.session.add(other_user)
        db.session.commit()

        self.assertEqual(user, User.find_by_username(user.username))

    def test_each_user_has_own_quips(self):
        circle = Circle('SF Crew')

        user = User('Jonathan Como', 'jcomo')
        user_quip = Quip('This is some thangs', user, circle)

        other_user = User('Peter Como', 'pcomo')
        other_user_quip = Quip('This is none thangs', other_user, circle)

        db.session.add(user_quip)
        db.session.add(other_user_quip)
        db.session.commit()

        self.assertEqual([user_quip], user.quips.all())
        self.assertEqual([other_user_quip], other_user.quips.all())

    def test_it_can_belong_to_many_circles(self):
        one_circle = Circle('SF Crew')
        other_circle = Circle('College Friends')

        user = User('Jonathan Como', 'jcomo')

        one_circle.add_member(user)
        other_circle.add_member(user)

        db.session.add(one_circle)
        db.session.add(other_circle)
        db.session.commit()

        self.assertEqual(sorted([one_circle, other_circle]), sorted(user.circles.all()))
