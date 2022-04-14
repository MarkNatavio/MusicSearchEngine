from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ml;kpCFGHVJHBNwezgdhxgfUIGYTRw32jchv,jhbk;iopooi0p9o8i67ru5e4y">:LPKJUIYT'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app