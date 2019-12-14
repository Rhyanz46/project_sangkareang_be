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
def show_job():
    pass
