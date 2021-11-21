from app import create_app
from settings import Config


app = create_app()
app.run(port=Config.PORT)
