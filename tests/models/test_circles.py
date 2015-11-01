from quipit.app import db
from quipit.models import User, Circle, Quip

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

    def test_it_can_have_many_quips(self):
        circle = Circle('SF Crew')

        user = User('Jonathan Como', 'jcomo')
        circle.add_member(user)

        quip = Quip('Some circle thangs?', user)
        other_quip = Quip('Some other thangs', user)

        circle.add_quip(quip)
        circle.add_quip(other_quip)

        db.session.add(circle)
        db.session.commit()

        self.assertEqual(sorted([quip, other_quip]), sorted(circle.quips.all()))

    def test_it_reports_number_of_quips(self):
        circle = Circle('SF Crew')

        user = User('Jonathan Como', 'jcomo')
        circle.add_member(user)

        quip = Quip('Some circle thangs?', user)
        other_quip = Quip('Some other thangs', user)

        circle.add_quip(quip)
        circle.add_quip(other_quip)

        self.assertEqual(2, circle.quip_count)

    def test_it_reports_number_of_members(self):
        circle = Circle('SF Crew')

        user = User('Jonathan Como', 'jcomo')
        other_user = User('Peter Como', 'pcomo')

        circle.add_member(user)
        circle.add_member(other_user)

        self.assertEqual(2, circle.member_count)
