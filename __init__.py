from flask import Flask
from urls import set_urls


def create_app():
    local_app = Flask(__name__)
    return local_app


if __name__ == "__main__":
    app = create_app()
    app = set_urls(app)
    app.run(port=8000, debug=True)
