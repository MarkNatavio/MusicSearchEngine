from crypt import methods
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .models import Artists, Playlists, Genres, Songs, Albums, Content

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  return render_template("home.html", user=current_user)

@views.route('/about', methods=['GET', 'POST'])
@login_required
def about():
  return render_template("about.html", user=current_user)

@views.route('/search', methods=['GET', 'POST'])
@login_required
def search(): 
  if request.method == "GET":
    songs_filtered = Songs.query.all()
    search_keyword = request.args.get('searchTextField')
    chosen_genre = request.args.get('genre_id')

    if chosen_genre: # search by genre
      songs_filtered = Songs.query.filter(Songs.genre == chosen_genre)
    elif search_keyword: # search by keyword
      songs_filtered = Songs.query.filter(Songs.song.contains(search_keyword))
    
    return render_template("search.html", user=current_user, genres=Genres.query.all(), artists=Artists.query.all(), songs=songs_filtered)
  
  else:
    check_song = request.form.get('song_selected')
    return redirect(url_for("views.info", song=check_song))


@views.route('/info/song_id/<song>', methods=['GET', 'POST'])
@login_required
def info(song):
  song_selected = Songs.query.filter(Songs.song_id == song).first()
  add_song_id = request.args.get('add_to_playlist')
  user_playlist_id = Playlists.query.filter(Playlists.user_id==current_user.user_id).first().playlist_id
  
  if add_song_id: # song is being added to playlist
    if Content.query.filter(Content.playlist_id==int(user_playlist_id), Content.song_id==int(add_song_id)).first() is None: # check if song already in playlist 
      new_playlist_song = Content(playlist_id=int(user_playlist_id), song_id=int(add_song_id))
      db.session.add(new_playlist_song)
      db.session.commit()

      flash('Song added to Favorites!', category='success')
      
    else: # song already in playlist
      flash('This song is already on your playlist', category='error')
    
  return render_template("info.html", user=current_user, song=song_selected, genres=Genres.query.all(), artists=Artists.query.all(), albums=Albums.query.all())


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
  account = request.form.get('user_id')
  if request.method == "POST":
    return redirect(url_for("views.edit_profile", id=account))
  
  return render_template("profile.html", user=current_user, playlist=Playlists.query.filter(Playlists.user_id == account))#, songs_saved=PlaylistsSongs.query.filter(PlaylistsSongs.song_id == Songs.song_id))


@views.route('/update/user/<id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
  return render_template("edit_profile.html", user=current_user, playlist=Playlists.query.filter(Playlists.user_id == id))#, songs_saved=PlaylistsSongs.query.filter(PlaylistsSongs.song_id == Songs.song_id))
