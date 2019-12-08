from flask import Blueprint

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/')
def index():
    return "hello comment"
