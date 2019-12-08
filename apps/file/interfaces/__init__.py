from flask import Blueprint

bp = Blueprint('file', __name__, url_prefix='/file')


@bp.route('/')
def index():
    return "hello file"
