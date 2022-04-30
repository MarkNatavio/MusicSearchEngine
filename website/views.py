from crypt import methods
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .models import Users, Playlists, Playlists_Songs, Genres, Songs, Albums

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
  if chosen_genre:
    songs_genre_filtered = Songs.query.filter(Songs.genre == chosen_genre)
    return render_template("search.html", user=current_user, genres=Genres.query.all(), songs=songs_genre_filtered)
  
  return render_template("search.html", user=current_user, genres=Genres.query.all(), songs=Songs.query.all())

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
  return render_template("profile.html", user=current_user)

@views.route('/info', methods=['GET', 'POST'])
@login_required
def info():
  return render_template("info.html", user=current_user)