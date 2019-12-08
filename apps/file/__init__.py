from .interfaces import bp


class FileModule:
    def __init__(self):
        from .models import File

    @staticmethod
    def init_app(app):
        app.register_blueprint(bp)
