from unittest import TestCase

from flask_testing import TestCase as FlaskTestCase

from quipit.app import app
from quipit.db import db


def _setup_db():
    db.create_all()


def _teardown_db():
    db.session.remove()
    db.drop_all()


class DBTestCase(TestCase):
    def setUp(self):
        super(DBTestCase, self).setUp()
        self.ctx = app.app_context()
        self.ctx.push()
        _setup_db()

    def tearDown(self):
        _teardown_db()
        self.ctx.pop()
        super(DBTestCase, self).tearDown()


class APITestCase(FlaskTestCase):
    def create_app(self):
        return app

    def setUp(self):
        super(APITestCase, self).setUp()
        app.config['TESTING'] = True
        _setup_db()

    def tearDown(self):
        _teardown_db()
        app.config['TESTING'] = False
        super(APITestCase, self).tearDown()
