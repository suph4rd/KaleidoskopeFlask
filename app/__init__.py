from flask import Flask
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from settings import Config
from .urls import set_urls


app = Flask(__name__)
app.config.from_object(Config)
app = set_urls(app)
