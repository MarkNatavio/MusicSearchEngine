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
  chosen_genre = request.form.get('genre_button')
  search_keyword = request.args.get('searchTextField')
  testing = request.form.get('song_selected')
  
  songs_genre_filtered = Songs.query.all()  

  if testing: # go to song info
    print(testing)
    return info(testing)
  elif chosen_genre: # search by genre
    print(chosen_genre)
    songs_genre_filtered = Songs.query.filter(Songs.genre == chosen_genre)
  elif search_keyword: # search by keyword
    print(search_keyword)
    songs_genre_filtered = Songs.query.filter(Songs.song.contains(search_keyword))
  
  
  return render_template("search.html", user=current_user, genres=Genres.query.all(), artists=Artists.query.all(), songs=songs_genre_filtered)


@views.route('/info', methods=['GET', 'POST'])
@login_required
def info(id):
  print(id)
  song_selected = Songs.query.filter(Songs.song_id == id).first()
  return render_template("info.html", user=current_user, song=song_selected, genres=Genres.query.all(), artists=Artists.query.all(), albums=Albums.query.all())


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
  return render_template("profile.html", user=current_user)
