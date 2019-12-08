from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from core.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(config)

    from core.cli import CLI
    from core.database import db

    from apps.user import UserModule
    from apps.post import PostModule
    from apps.comment import CommentModule
    from apps.category import CategoryModule
    from apps.file import FileModule

    cli = CLI()
    cors = CORS()
    migrate = Migrate()

    user = UserModule()
    post = PostModule()
    comment = CommentModule()
    category = CategoryModule()
    file = FileModule()

    cli.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    user.init_app(app)
    post.init_app(app)
    comment.init_app(app)
    category.init_app(app)
    file.init_app(app)

    return app
