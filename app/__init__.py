from flask import Flask
from flask_login import LoginManager

from datetime import datetime
import time

login_manager = LoginManager()
SERVER_START_TIME = datetime.now()

from .auth import User

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in {'test'} else None

def create_app():
    app = Flask(__name__)

    SERVER_START_TIME = datetime.now()
    app.config['SECRET_KEY'] = 'supersecret'

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    from .routes import main
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
