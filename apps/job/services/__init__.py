from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Job, user_jobs, JobCategory
from apps.user.models import User
from apps.category_access.models import CategoryAccess


@jwt_required
def create_job(data):
    job_ca_ = JobCategory.query.filter_by(id=data['category_id']).first()
    if not job_ca_:
        return {"message": "category id is not found"}, 400
    job = Job(
        name=data['name'],
        description=data['description'],
        start_time=data['start_time'],
        deadline=data['deadline'],
        category_id=data['category_id']
    )
    user = User.query.filter_by(id=get_jwt_identity()).first()
    if not user:
        return {"message": "user authentication is wrong"}, 400

    ca = CategoryAccess.query.filter_by(id=user.category_access_id).first()
    if not ca:
        return {"message": "you permission is not setup"}, 403

    if not ca.add_job:
        return {"message": "you not have permission"}, 403

    job_not_done_exist = Job.query.\
        join(user_jobs).\
        join(User).filter(
            User.id == user.id,
            Job.name == job.name,
            Job.done == False
        ).first()

    if job_not_done_exist:
        return {"message": "you must finish '{}' job first, to create new one with same name".format(job.name)}, 400

    try:
        job.users.append(user)
        job.commit()
    except:
        return {"message": "failed to save job, tell you software engineer"}, 500
    return {"message": "success create {} job".format(job.name)}


@jwt_required
def my_job_list(done=None):
    user = User.query.filter_by(id=get_jwt_identity()).first()
    if not user:
        return {"message": "user authentication is wrong"}, 400

    ca = CategoryAccess.query.filter_by(id=user.category_access_id).first()
    if not ca:
        return {"message": "you permission is not setup"}, 403

    if not ca.show_job:
        return {"message": "you not have permission"}, 403

    if isinstance(done, type(None)):
        jobs = Job.query. \
            join(user_jobs). \
            join(User).filter(
                User.id == user.id
            )

        if not jobs.first():
            return {"message": "you have not jobs"}, 204

        my_jobs = []

        for job in jobs.all():
            my_jobs.append(job.__serialize__())

        return {"data": my_jobs}
    return {"message": "this feature is not finish"}, 400


@jwt_required
def detail_job(job_id, data=None, mode=None):
    user = User.query.filter_by(id=get_jwt_identity()).first()
    if not user:
        return {"message": "user authentication is wrong"}, 400

    ca = CategoryAccess.query.filter_by(id=user.category_access_id).first()
    if not ca:
        return {"message": "you permission is not setup"}, 403

    job = Job.query.filter_by(id=job_id).first()

    if not job:
        return {"message": "job is not found"}, 400

    if mode == 'edit':
        one_value = len(list(set(data.values()))) == 1
        null = isinstance(None, type(list(set(data.values()))[0]))
        if one_value and null:
            return {"message": "kamu harus mempunyai data untuk mengedit"}, 400
        if not ca.update_job:
            return {"message": "you not have permission"}, 403
        if not isinstance(None, type(data['name'])):
            job.name = data['name']
        if not isinstance(None, type(data['description'])):
            job.description = data['description']
        if not isinstance(None, type(data['start_time'])):
            job.start_time = data['start_time']
        if not isinstance(None, type(data['deadline'])):
            job.deadline = data['deadline']
        if not isinstance(None, type(data['status'])):
            job.status = data['status']
        if not isinstance(None, type(data['done'])):
            if not job.done:
                job.done = data['done']
            else:
                if not ca.root_access:
                    return {"error": "you can't edit done status for this job :)"}, 400
                job.done = data['done']

        try:
            job.commit()
        except:
            return {"message": "error to edit, tell you software engineer!!"}, 500
        return {"message": "success to edit"}
    if mode == 'delete':
        if not ca.delete_job:
            return {"message": "you not have permission"}, 403
        try:
            job.delete()
        except:
            return {"message": "error to delete, tell you software engineer!!"}, 500
        return {"message": "success to delete"}
    return {'data': job.__serialize__()}


@jwt_required
def job_ca(name, mode=None):
    ca = JobCategory.query.filter_by(name=name).first()
    if mode == 'delete':
        if not ca:
            return {"error": "kategori {} tidak ada".format(name)}, 400
        try:
            ca.delete()
        except:
            return {"error": "terjadi kesalahan saat menghapus, tanyakan masalah ini ke backend".format(name)}, 500
        return {"message": "sukses"}
    if ca:
        return {"error": "kategori sudah ada"}, 400
    job_ca_ = JobCategory(
        name=name
    )
    try:
        job_ca_.commit()
    except:
        return {"message": "error untuk membuat, "
                           "perhatikan ketentuan pembuatan "
                           "kategori apakah sudah benar"}, 500
    return {"message": "success"}


@jwt_required
def job_ca_list(page):
    if not page:
        page = 1
    try:
        page = int(page)
    except:
        return {"error": "parameter page must be integer"}, 400
    job_ca_list_ = JobCategory.query.paginate(per_page=20, page=page)

    if not job_ca_list_.total:
        return {"message": "no user found at this category permission"}, 400

    result = []
    for item in job_ca_list_.items:
        result.append({"user_id": item.id, "name": item.name})

    meta = {
        "total_data": job_ca_list_.total,
        "total_pages": job_ca_list_.pages,
        "total_data_per_page": job_ca_list_.per_page,
        "next": "?page={}".format(job_ca_list_.next_num) if job_ca_list_.has_next else None,
        "prev": "?page={}".format(job_ca_list_.prev_num) if job_ca_list_.has_prev else None
    }
    return {"data": result, "meta": meta}
