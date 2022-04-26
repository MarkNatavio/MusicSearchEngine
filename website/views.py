from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

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
  return render_template("search.html", user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
  return render_template("profile.html", user=current_user)

@views.route('/info', methods=['GET', 'POST'])
@login_required
def info():
  return render_template("info.html", user=current_user)