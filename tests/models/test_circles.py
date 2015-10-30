from quipit.app import db
from quipit.models import User, Circle

from tests.test_case import DBTestCase


class CircleTestCase(DBTestCase):
    def test_it_can_add_members_without_saving(self):
        circle = Circle('SF Crew')

        user = User('Jonathan Como', 'jcomo')
        other_user = User('Peter Como', 'pcomo')

        circle.add_member(user)
        self.assertEqual(1, len(circle.members.all()))

        circle.add_member(other_user)
        self.assertEqual(2, len(circle.members.all()))

        self.assertIsNone(circle.id)

    def test_it_does_not_add_duplicate_members(self):
        circle = Circle('SF Crew')
        user = User('Jonathan Como', 'jcomo')

        circle.add_member(user)
        circle.add_member(user)

        self.assertEqual(1, len(circle.members.all()))

    def test_it_can_have_many_members(self):
        circle = Circle('SF Crew')

        user = User('Jonathan Como', 'jcomo')
        other_user = User('Peter Como', 'pcomo')

        circle.add_member(user)
        circle.add_member(other_user)

        db.session.add(circle)
        db.session.commit()

        self.assertEqual(sorted([user, other_user]), sorted(circle.members.all()))
