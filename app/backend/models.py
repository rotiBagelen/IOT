from . import db
from sqlalchemy.sql import func

class Taplog(db.Model):
    __tablename__ = 'taplog'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(100))
    card_id = db.Column(db.String(50), nullable=False)
    userName = db.Column(db.String(50), nullable=False)

class Temperature(db.Model):
    __tablename__ = 'temperature'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(100))
    temperature = db.Column(db.Float, nullable=False)

class cardID(db.Model):
    __tablename__ = 'card_table'
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.String(50), nullable=False, unique=True)
    userName = db.Column(db.String(50), nullable=False)