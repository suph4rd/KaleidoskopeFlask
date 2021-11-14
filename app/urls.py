from app import views


def set_urls(app):
    app.add_url_rule('/', view_func=views.index)
    app.add_url_rule('/media/<filename>', view_func=views.media)
    return app