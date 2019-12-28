from datetime import date
from flask import Blueprint, request
from core import method_is, parser

from ..services import create_job, my_job_list, detail_job, job_cat, job_cat_list, users_of_job

bp = Blueprint('job', __name__, url_prefix='/job')


@bp.route('', methods=['POST', 'GET'])
def index():
    if method_is('POST'):
        data = parser.ValueChecker(request.json)
        data.parse('name', str, length=100)
        data.parse('description', str, nullable=True, length=300)
        data.parse('start_time', date, length=100)
        data.parse('deadline', date, nullable=True, length=100)
        data.parse('done', bool, nullable=True, length=100)

        data.parse('nilai_material', str, nullable=True, length=255)
        data.parse('nilai_jasa', str, nullable=True, length=255)

        data.parse('job_location', str, nullable=True, length=255)
        data.parse('no_spk', str, nullable=True, length=255)
        data.parse('given_by', str, length=255)
        data.parse('category_id', int, length=11)

        data.parse('users', list, nullable=True)
        return create_job(data.get_parsed())
    return my_job_list()


@bp.route('<int:job_id>', methods=['PUT', 'GET', 'DELETE'])
def job_detail(job_id):
    if method_is('GET'):
        return detail_job(job_id)
    if method_is('DELETE'):
        return detail_job(job_id, mode='delete')

    data = parser.ValueChecker(request.json)
    data.parse('name', str, nullable=True, length=100)
    data.parse('description', str, nullable=True, length=300)
    data.parse('start_time', date, nullable=True, length=100)
    data.parse('deadline', date, nullable=True, length=100)
    data.parse('done', bool, nullable=True, length=100)
    return detail_job(job_id, data.get_parsed(), mode='edit')


@bp.route('/category', methods=['POST', 'GET'])
def job_cat_handler():
    if method_is('GET'):
        return job_cat_list(request.args.get('page'))
    data = parser.ValueChecker(request.json)
    data.parse('name', str, length=200)
    return job_cat(data.get_parsed()['name'])


@bp.route('/category/<string:name>', methods=['DELETE'])
def job_cat_detail_handler(name):
    return job_cat(name, mode='delete')


@bp.route('<int:job_id>/users', methods=['PUT', 'GET', 'DELETE'])
def job_users(job_id):
    return users_of_job(job_id)
