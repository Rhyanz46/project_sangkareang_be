from flask import Blueprint

bp = Blueprint('job', __name__, url_prefix='/job')


@bp.route('/')
def index():
    return "hello file"
