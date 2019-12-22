from flask import Blueprint, request
from core import method_is, parser
from ..services import set_ca, get_list_ca, edit_ca, set_user, user_of_ca

bp = Blueprint('category_access', __name__, url_prefix='/category-access')


@bp.route('', methods=['POST', 'GET'])
def ca():
    if method_is('GET'):
        return get_list_ca()
    data = parser.ValueChecker(request.json)
    data.parse('name', field_type=str, length=30)
    data.parse('add_user', field_type=bool, length=10)
    data.parse('delete_user', field_type=bool, length=10)
    data.parse('edit_user', field_type=bool, length=10)
    data.parse('add_job', field_type=bool, length=10)
    data.parse('delete_job', field_type=bool, length=10)
    data.parse('update_job', field_type=bool, length=10)
    data.parse('show_job', field_type=bool, length=10)
    data.parse('print_job', field_type=bool, length=10)
    data.parse('check_job', field_type=bool, length=10)
    data.parse('service_job', field_type=bool, length=10)
    return set_ca(data.get_parsed())


@bp.route('/<int:id>', methods=['PUT', 'GET'])
def ca_detail(id):
    if method_is('GET'):
        return get_list_ca(id=id)
    data = parser.ValueChecker(request.json)
    data.parse('name', nullable=True, field_type=str, length=30)
    data.parse('add_user', nullable=True, field_type=bool, length=10)
    data.parse('delete_user', nullable=True, field_type=bool, length=10)
    data.parse('edit_user', nullable=True, field_type=bool, length=10)
    data.parse('add_job', nullable=True, field_type=bool, length=10)
    data.parse('delete_job', nullable=True, field_type=bool, length=10)
    data.parse('update_job', nullable=True, field_type=bool, length=10)
    data.parse('show_job', nullable=True, field_type=bool, length=10)
    data.parse('print_job', nullable=True, field_type=bool, length=10)
    data.parse('check_job', nullable=True, field_type=bool, length=10)
    data.parse('service_job', nullable=True, field_type=bool, length=10)
    return edit_ca(id, data.get_parsed())


@bp.route('/<string:ca_name>/<int:user_id>', methods=['POST'])
def set_ca_user(ca_name, user_id):
    data = parser.ValueChecker(request.json)
    data.parse('action', field_type=str, enum=["on", "off"], length=30)
    return set_user(ca_name, user_id, data.get_parsed())


@bp.route('/<string:ca_name>/userlist', methods=['GET'])
def get_user_ca_list(ca_name):
    return user_of_ca(ca_name)
