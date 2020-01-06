from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import User
from apps.job.models import Job, user_jobs
from apps.category_access.models import CategoryAccess


@jwt_required
def user_list(page, job_accept):
    current_user = User.query.filter_by(id=get_jwt_identity()).first()
    if not current_user:
        return {"message": "user authentication is wrong"}, 400

    ca = CategoryAccess.query.filter_by(id=current_user.category_access_id).first()
    if not ca:
        return {"message": "you permission is not setup"}, 403

    if not ca.root_access:
        return {"message": "only for root access can do this"}, 400

    if not page:
        page = 1
    try:
        page = int(page)
    except:
        return {"message": "page param must be integer"}, 400

    if job_accept and job_accept.lower() == 'false':
        users = User\
            .query\
            .join(user_jobs)\
            .join(Job)\
            .filter(
                Job.accepted == False,
                Job.done == False
            )\
            .paginate(page=page, per_page=30)
        if not users.total:
            return {"message": "tidak ada karyawan yang pekerjaannya belum di verifikasi"}, 204
    else:
        users = User.query.paginate(page=page, per_page=30)
        if not users.total:
            return {"message": "belum ada pekerja, kamu bisa mendaftarkan pekerja baru"}, 204

    result = []
    for user in users.items:
        ca_ = CategoryAccess.query.filter_by(id=user.category_access_id).first()
        data = user.__serialize__(True)
        data.update({"category_access_name": ca_.name})
        result.append(data)

    meta = {
        "total_data": users.total,
        "total_pages": users.pages,
        "total_data_per_page": users.per_page,
        "next": "?page={}".format(users.next_num) if users.has_next else None,
        "prev": "?page={}".format(users.prev_num) if users.has_prev else None
    }
    return {"data": result, "meta": meta}


