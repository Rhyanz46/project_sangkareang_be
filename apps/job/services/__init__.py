from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Job, user_jobs
from apps.user.models import User
from apps.category_access.models import CategoryAccess


@jwt_required
def create_job(data):
    job = Job(
        name=data['name'],
        description=data['description'],
        start_time=data['start_time'],
        deadline=data['deadline']
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

    if mode == 'edit' and not isinstance(None, type(None)):
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
