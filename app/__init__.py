from flask import Flask
from dotenv import load_dotenv, find_dotenv
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

from settings import Config


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    from app import models

    login_manager.init_app(app)
    from app import views
    app.add_url_rule('/', view_func=views.index)
    app.add_url_rule('/admin-panel', view_func=views.admin_panel)
    app.add_url_rule('/login', view_func=views.login, methods=['post', 'get'])
    app.add_url_rule('/logout', view_func=views.logout)
    app.add_url_rule('/media/<filename>', view_func=views.media)

    return app

