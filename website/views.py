#from crypt import methods
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .models import Artists, Playlists, Genres, Songs, Albums, Content, Users

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
  if request.method == "GET":
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
  account = current_user.user_id
  if request.method == "POST":
    return redirect(url_for("views.edit_profile", id=account))
  
  return render_template("profile.html", user=current_user, playlists=Playlists.query.filter(Playlists.user_id == account), content=Content.query.all(), songs=Songs.query.all(), genres=Genres.query.all(), artists=Artists.query.all(), albums=Albums.query.all())


@views.route('/update_user/<id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
  if int(id) != int(current_user.user_id): # do not allow other users to edit someone else's page
    flash('You cannot access this page', category='error')
    return redirect(url_for("views.home", user=current_user))
  
  else: # allow current user to edit their own pag      
    new_username = current_user.username
    new_email = current_user.email
    new_bio = current_user.bio
    #new_password = current_user.password
    
    if request.method == "GET":
      delete_vals = request.args.get('song_to_delete')
      if delete_vals: # delete songs in playlist
        arr = delete_vals.split(',')
        delete_playlist_id = int(arr[0])
        delete_song_id = int(arr[1])
        entry_to_delete = Content.query.filter(Content.playlist_id==delete_playlist_id, Content.song_id==delete_song_id).first()
        db.session.delete(entry_to_delete)
        db.session.commit()
        
      else: # update info
        new_username = request.args.get('new_username')
        new_email = request.args.get('new_email')
        new_bio = request.args.get('new_bio')
        # new_password = request.args.get('new_password')
        acceptable = 1
      
        if new_username:
          user = Users.query.filter(Users.user_id == current_user.user_id).first()
          user.username = new_username
          db.session.commit()
          acceptable = 2
          
        if new_email:
          account = Users.query.filter_by(email=new_email).first()
          if account and new_email!=current_user.email:
            acceptable = 0
            flash('There is already an account with this email.', category='error')
          elif len(new_email) < 4:
            acceptable = 0
            flash('Invalid email address. Email address must follow \'email@example.com\' format.', category='error')
          else:
            user = Users.query.filter(Users.user_id == current_user.user_id).first()
            user.email = new_email
            db.session.commit()
            acceptable = 2
          
        # if new_password:
        #   user = Users.query.filter(Users.user_id == current_user.user_id).first()
        #   user.password = new_password
        #   db.session.commit()
        #   acceptable = 2
          
        if new_bio:
          user = Users.query.filter(Users.user_id == current_user.user_id).first()
          user.bio = new_bio
          db.session.commit()
          acceptable = 2
        
        if acceptable == 2:
          flash('Changes have been saved!', category='successs')
        
        
    return render_template("edit_profile.html", user=current_user, playlists=Playlists.query.filter(Playlists.user_id == id), content=Content.query.all(), songs=Songs.query.all(), genres=Genres.query.all(), artists=Artists.query.all(), albums=Albums.query.all())
      