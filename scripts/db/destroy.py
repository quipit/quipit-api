from quipit.app import app
from quipit.db import db

with app.app_context():
    db.drop_all()
