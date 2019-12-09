from flask import Blueprint

bp = Blueprint('category_access', __name__, url_prefix='/category-access')


@bp.route('/')
def index():
    return "hello file"
