from quipit.app import db
from quipit.models import User, Circle, Quip

from tests.test_case import DBTestCase


class CircleTestCase(DBTestCase):
    def setUp(self):
        super(CircleTestCase, self).setUp()
        self.user = User('Jonathan Como', 'jcomo')
        self.circle = Circle('SF Crew')
        self.circle.add_member(self.user)

    def test_it_does_not_add_duplicate_members(self):
        self.circle.add_member(self.user)

        self.assertEqual(1, self.circle.member_count)

    def test_it_can_have_many_members(self):
        other_user = User('Peter Como', 'pcomo')

        self.circle.add_member(other_user)

        db.session.add(self.circle)
        db.session.commit()

        self.assertEqual(sorted([self.user, other_user]), sorted(self.circle.members.all()))

    def test_it_does_not_add_duplicate_quips(self):
        quip = Quip('Some circle thangs?', self.user)

        self.circle.add_quip(quip)
        self.circle.add_quip(quip)

        self.assertEqual(1, self.circle.quip_count)

    def test_it_can_have_many_quips(self):
        quip = Quip('Some circle thangs?', self.user)
        other_quip = Quip('Some other thangs', self.user)

        self.circle.add_quip(quip)
        self.circle.add_quip(other_quip)

        db.session.add(self.circle)
        db.session.commit()

        self.assertEqual(sorted([quip, other_quip]), sorted(self.circle.quips.all()))
