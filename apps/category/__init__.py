from .interfaces import bp


class CategoryModule:
    def __init__(self):
        from .models import Category

    @staticmethod
    def init_app(app):
        app.register_blueprint(bp)
