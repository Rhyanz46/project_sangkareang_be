from .interfaces import bp


class UserModule:
    def __init__(self):
        from .models import User

    @staticmethod
    def init_app(app):
        app.register_blueprint(bp)
