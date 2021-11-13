from flask import render_template


def model():
    from app import models
    return models


def index():
    footer_obj = model().Footer.query.order_by(model().Footer.id.desc()).first()
    return render_template('index.html', **locals())
