from unittest import TestCase

from quipit.app import db


class DBTestCase(TestCase):
    def setUp(self):
        super(DBTestCase, self).setUp()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        super(DBTestCase, self).tearDown()
