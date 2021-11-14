import datetime
import sqlalchemy_utils as sa_utils
from sqlalchemy.sql import func

from app import db


class CreateUpdateMixin:
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


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
