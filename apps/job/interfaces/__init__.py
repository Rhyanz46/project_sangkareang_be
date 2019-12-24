from datetime import date
from flask import Blueprint, request
from core import method_is, parser

from ..services import create_job, my_job_list, detail_job

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
    return my_job_list()


@bp.route('<int:job_id>', methods=['PUT', 'GET'])
def job_detail(job_id):
    if method_is('GET'):
        return detail_job(job_id)
    data = parser.ValueChecker(request.json)
    data.parse('name', str, nullable=True, length=100)
    data.parse('description', str, nullable=True, length=300)
    data.parse('start_time', date, nullable=True, length=100)
    data.parse('deadline', date, nullable=True, length=100)
    data.parse('status', bool, nullable=True, length=100)
    data.parse('done', bool, nullable=True, length=100)
    return detail_job(job_id, data.get_parsed(), mode='edit')
