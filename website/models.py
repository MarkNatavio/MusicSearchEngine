from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Artists(db.Model):
  artist_id = db.Column(db.Integer, primary_key=True)
  artist = db.Column(db.String(255))
  
  
class Genres(db.Model):
  genre_id = db.Column(db.Integer, primary_key=True)
  genre = db.Column(db.String(255))
  
  
class Albums(db.Model):
  album_id = db.Column(db.Integer, primary_key=True)
  album = db.Column(db.String(255))
  album_date = db.Column(db.Integer)
  artist = db.Column(db.String(255))


class Songs(db.Model):
  song_id = db.Column(db.Integer, primary_key=True)
  song = db.Column(db.String(255))
  artist = db.Column(db.Integer, db.ForeignKey('artists.artist_id'))
  genre = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
  album = db.Column(db.Integer, db.ForeignKey('albums.album_id'))
  album_date = db.Column(db.Integer)
  duration = db.Column(db.String(4))
  lyrics = db.Column(db.Text)


class Users(db.Model, UserMixin):
  user_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  password = db.Column(db.String(255))
  email = db.Column(db.String(255), unique=True)
  bio = db.Column(db.String(255))
  
  def get_id(self):
    return self.user_id


class Playlists(db.Model):
  playlist_id = db.Column(db.Integer, primary_key=True)
  playlist_name = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

  
class Playlists_Songs(db.Model):
  row_id = db.Column(db.Integer, primary_key=True)
  song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'))
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'))