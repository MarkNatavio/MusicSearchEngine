from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Songs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  genres = db.Column(db.String(255))
  release_date = db.Column(db.DateTime(timezone=True), default=func.now())
  users = db.relationship('User_Song_List')

class User_Song_List(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  songs_id = db.Column(db.Integer, db.ForeignKey('songs.id'))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255))
  username = db.Column(db.String(255))
  song_list = db.relationship('User_Song_List')
  
  