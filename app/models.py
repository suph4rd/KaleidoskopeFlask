import datetime
import enum

import sqlalchemy_utils as sa_utils
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class CreateUpdateMixin:
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.id}>"


class Footer(db.Model, CreateUpdateMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class Content(db.Model, CreateUpdateMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    link = db.Column(sa_utils.URLType)
    img = db.Column(sa_utils.URLType)


class RoleEnum(enum.Enum):
    common = 'common'
    admin = 'admin'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class User(db.Model, CreateUpdateMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    patronymic = db.Column(db.String(255))
    role = db.Column(db.Enum(RoleEnum), default=0, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        print(self.password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
