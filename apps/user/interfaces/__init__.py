from datetime import date
from flask import Blueprint, request

from core import method_is, parser

from ..services import register, login, update, show_user_detail

bp = Blueprint('user', __name__, url_prefix='/user')

ddd = [
    {"message": "Welcome"}
]


@bp.route('', methods=['GET', 'POST'])
def index():
    data = parser.ValueChecker(request.json)
    data.parse('username', field_type=str, length=30)
    data.parse('email', field_type=str, length=30)
    data.parse('fullname', field_type=str, length=30)
    data.parse('address', field_type=str, length=30)
    data.parse('phone_number', field_type=int, length=30)
    data.parse('work_start_time', field_type=date, length=30)
    data.parse('activate', field_type=bool, length=30)
    data.parse('password', field_type=str, length=30)

    if method_is('POST'):
        return register(data.get_parsed())
    return {"message": "waw"}, 200


@bp.route('/auth', methods=['GET', 'POST'])
def auth():
    data = parser.ValueChecker(request.json)
    data.parse('username', field_type=str, length=30)
    data.parse('password', field_type=str, length=30)

    if method_is('POST'):
        return login(data.get_parsed())
    return {"message": "waw"}, 200


@bp.route('/detail/<string:username>', methods=['PUT', 'GET'])
def do_update(username):
    data = parser.ValueChecker(request.json)
    data.parse('username', field_type=str, nullable=True, length=30)
    data.parse('email', field_type=str, nullable=True, length=30)
    data.parse('fullname', field_type=str, nullable=True, length=30)
    data.parse('address', field_type=str, nullable=True, length=30)
    data.parse('phone_number', field_type=int, nullable=True, length=30)
    data.parse('work_start_time', field_type=date, nullable=True,  length=30)
    data.parse('activate', field_type=bool, nullable=True,  length=30)
    data.parse('password', field_type=str, nullable=True, length=30)

    if method_is('PUT'):
        return update(username, data.get_parsed())
    elif method_is('GET'):
        return show_user_detail(username)
    return {"message": "waw"}, 200
