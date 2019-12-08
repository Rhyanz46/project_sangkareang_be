from flask import Blueprint

bp = Blueprint('category', __name__, url_prefix='/category')


@bp.route('/')
def index():
    return "hello category"
