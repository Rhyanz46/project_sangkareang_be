from flask import Blueprint, request
from core import method_is, parser
from ..services import set_access_user

bp = Blueprint('category_access', __name__, url_prefix='/category-access')


@bp.route('', methods=['POST'])
def index():
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
    return set_access_user(data.get_parsed())
