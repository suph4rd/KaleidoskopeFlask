from app import views


def set_urls(app):
    app.add_url_rule('/', view_func=views.index)
    return app