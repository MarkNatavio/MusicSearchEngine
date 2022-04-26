from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True)
  password = db.Column(db.String(255))
  username = db.Column(db.String(255))
  notes = db.relationship('Note')


class Songs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  release_date = db.Column(db.DateTime(timezone=True), default=func.now())
  users = db.relationship('User_Song_List')
  genres = db.relationship('Genres')

class Genres(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  song_name = db.Column(db.String(255), db.ForeignKey('songs.id'))
  genre_name = db.Column(db.String(255))

class User_Song_List(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  songs_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
  

  
  