from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password1')
    
    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        return redirect(url_for('views.home'))
      else:
        flash('Incorrect password. Try again', category='error')
    else:
      flash('Email is incorrect or does not exist.', category='error')
  
  return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
  return render_template("logout.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
  if request.method == 'POST':  
    email = request.form.get('email')
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    user = User.query.filter_by(email=email).first()
    
    if user:
      flash('There is already an account with this email.', category='error')
    elif len(email) < 4:
      flash('Invalid email address. Email address must follow \'email@example.com\' format.', category='error')
    elif len(username) < 2:
      flash('Invalid username. Username is too short. (it must be greater than 1 character).', category='error')
    elif password1 != password2:
      flash('Error. Passwords do not match.', category='error')
    elif len(password1) < 7:
      flash('Invalid password. Your password is too short (it must be at least 7 characters).', category='error')
    else:
      new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
      db.session.add(new_user)
      db.session.commit()
      flash('Account created!', category='success')
      
      return redirect(url_for('views.home'))
      
  return render_template("signup.html")