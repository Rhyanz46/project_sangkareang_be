from flask import Blueprint

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/')
def index():
    return "hello post"
