# import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# from website import dbinfo

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'nabhjkdsvuscbhkjnkbfacjk akavssdoib j'
    # content = "mysql+pymysql://{0}:{1}@{2}/{3}".format(dbinfo.dbuser, dbinfo.dbpass, dbinfo.dbhost, dbinfo.dbname, pool_size=25, max_overflow=0)
    # app.config['SQLALCHEMY_DATABASE_URI'] = content
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db = SQLAlchemy(app)
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note, Songs, User_Song_List
    
    create_db(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_db(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
