import os

base_dir = os.getcwd()


class Config:
    DEBUG = os.getenv("DEBUG", True)
    ENV = os.getenv("ENV", "DEVELOPMENT")
    SECRET_KEY = os.getenv("SECRET_KEY", "SDSADWE33C32R32FV34FC32Q3XD23XFD3DEWD")
    PORT = os.getenv("PORT", "8000")

    # database
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/db/proj.db"
