import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'nabhjkdsvuscbhkjnkbfacjk akavssdoib j'
    
    connection = "mysql+pymysql://{0}:{1}@{2}/{3}".format('root', 'password1234', 'localhost', 'MusicDB', pool_size=25, max_overflow=0)
    app.config['SQLALCHEMY_DATABASE_URI'] = connection    
    
    db = SQLAlchemy(app)
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import Users, Songs, Artists, Genres, Albums, Playlists, Content
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    return app
