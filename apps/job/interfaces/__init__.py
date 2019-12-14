from datetime import date
from flask import Blueprint, request
from core import method_is, parser

from ..services import create_job, show_job

bp = Blueprint('job', __name__, url_prefix='/job')


@bp.route('', methods=['POST', 'GET'])
def index():
    if method_is('POST'):
        data = parser.ValueChecker(request.json)
        data.parse('name', str, length=100)
        data.parse('description', str, nullable=True, length=300)
        data.parse('start_time', date, length=100)
        data.parse('deadline', date, nullable=True, length=100)
        data.parse('status', bool, nullable=True, length=100)
        return create_job(data.get_parsed())
    return show_job()
