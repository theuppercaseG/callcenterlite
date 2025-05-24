from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class CallLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_number = db.Column(db.String(20))
    status = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
