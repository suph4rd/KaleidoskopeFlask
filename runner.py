from app import app
from settings import Config


if __name__ == '__main__':
    app.run(port=Config.PORT)
