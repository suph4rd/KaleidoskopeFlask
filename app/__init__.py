from flask import Flask
from dotenv import load_dotenv, find_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

from settings import Config
from .urls import set_urls


app = Flask(__name__)
app.config.from_object(Config)
app = set_urls(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import models
