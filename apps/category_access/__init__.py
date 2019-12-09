from .interfaces import bp


class CategoryAccessModule:
    def __init__(self):
        from .models import CategoryAccess

    @staticmethod
    def init_app(app):
        app.register_blueprint(bp)
