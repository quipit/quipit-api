from unittest import TestCase

from quipit.app import app
from quipit.db import db


class DBTestCase(TestCase):
    def setUp(self):
        super(DBTestCase, self).setUp()
        self.ctx = app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()
        super(DBTestCase, self).tearDown()
