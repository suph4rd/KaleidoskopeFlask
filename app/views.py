from flask import render_template, send_from_directory, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from six import wraps

from . import forms, models


def context(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        footer_obj = models.Footer.query.order_by(models.Footer.id.desc()).first()
        # content_qs = model().Content.query.order_by(model().Content.type.asc()).all()
        content_qs = models.Content.query.all()
        return func(footer_obj=footer_obj, content_qs=content_qs, *args, **kwargs)
    return wrapper


@context
def index(*args, **kwargs):
    variables = locals()
    variables.update(kwargs)
    return render_template('index.html', **variables)
    # return render_template('index.html', **locals())


@login_required
@context
def admin_panel(*args, **kwargs):
    variables = locals()
    variables.update(kwargs)
    return render_template('index.html', **variables)


@context
def login(*args, **kwargs):
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = forms.LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter(models.User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("admin_panel"))
        flash("Invalid username or password!", "error")
        return redirect(url_for("login"))
    variables = locals()
    variables.update(kwargs)
    return render_template('login.html', **variables)


def logout(*args, **kwargs):
    logout_user()
    return redirect(url_for("index"))


def media(filename, *args, **kwargs):
    from settings import Config
    path = Config.UPLOAD_FOLDER
    file = send_from_directory(path, filename)
    return file
