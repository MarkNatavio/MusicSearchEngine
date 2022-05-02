from crypt import methods
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .models import Artists, Playlists, Playlists_Songs, Genres, Songs, Albums

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
  add_song = request.form.get('add_to_playlist')
  if add_song:
    print(add_song)
  return render_template("info.html", user=current_user, song=song_selected, genres=Genres.query.all(), artists=Artists.query.all(), albums=Albums.query.all())


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
  return render_template("profile.html", user=current_user)
