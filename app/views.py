from flask import render_template, send_from_directory


def model():
    from app import models
    return models


def index():
    footer_obj = model().Footer.query.order_by(model().Footer.id.desc()).first()
    # content_qs = model().Content.query.order_by(model().Content.type.asc()).all()
    content_qs = model().Content.query.all()
    return render_template('index.html', **locals())


def media(filename):
    from app import app
    path = app.config.get('UPLOAD_FOLDER')

    x = send_from_directory(path, filename)
    return x