from .interfaces import bp


class JobModule:
    def __init__(self):
        from .models import Job

    @staticmethod
    def init_app(app):
        app.register_blueprint(bp)
