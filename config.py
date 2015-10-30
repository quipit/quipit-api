import os

# Used for debugging the ORM - shows all db statements
SQLALCHEMY_ECHO = bool(os.environ.get('SQLALCHEMY_ECHO', False))
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
