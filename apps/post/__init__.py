from .interfaces import bp


class PostModule:
    def __init__(self):
        from .models import Post

    @staticmethod
    def init_app(app):
        app.register_blueprint(bp)
