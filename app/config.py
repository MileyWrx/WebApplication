import os

from flask import app
from flask_sqlalchemy import SQLAlchemy
#SCRF Protection was enabled
WTF_CSRF_ENABLED = True
#CSRF encryption key was set
SECRET_KEY = '1BCDEFGHIJKLMNOPQRSTUVWXYZ12345'


basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

db = SQLAlchemy(app)