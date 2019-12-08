from .interfaces import bp


class CommentModule:
    def __init__(self):
        from .models import Comment

    @staticmethod
    def init_app(app):
        app.register_blueprint(bp)
