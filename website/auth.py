from email import message
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
  return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
  return render_template("logout.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
  if request.method == 'POST':  
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password1')
    password2 = request.form.get('password2')
    
    if len(email) < 4:
      flash('Invalid email address. Email address must follow \'email@example.com\' format.', category='error')
    elif len(username) < 2:
      flash('Invalid username. Username is too short. (it must be greater than 1 character).', category='error')
    elif password != password2:
      flash('Error. Passwords do not match.', category='error')
    elif len(password) < 7:
      flash('Invalid password. Your password is too short (it must be at least 7 characters).', category='error')
    else:
      flash('Account created!', category='success')
      #add users
  return render_template("signup.html")