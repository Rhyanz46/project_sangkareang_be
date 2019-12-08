from flask import Blueprint, request

from core import method_is, parser

from ..services import register

bp = Blueprint('user', __name__, url_prefix='/user')

ddd = [
    {"message": "Welcome"}
]


@bp.route('', methods=['GET', 'POST'])
def index():
    data = parser.ValueChecker(request.json)
    data.parse('username', field_type=str, length=30)
    data.parse('email', field_type=str, length=30)
    data.parse('password', field_type=str, length=30)

    if method_is('POST'):
        return register(data.parse())
    return {"message": "waw"}, 200
