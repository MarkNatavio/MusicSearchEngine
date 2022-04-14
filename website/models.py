from pytz import timezone
from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Songs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  genres = db.Column(db.String(10000))
  release_date = db.Column(db.DataTime(timezone=True), default=func.now())

class Songs_Per_User(db.Model):
  userid = db.Column(db.Integer, db.ForeignKey('user.id'))
  songid = db.Column(db.Integer, db.ForeignKey('songs.id'))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255))
  username = db.Column(db.String(255))
  song = db.relationship('Songs')
  
  