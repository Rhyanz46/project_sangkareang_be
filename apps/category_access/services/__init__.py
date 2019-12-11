from flask_jwt_extended import jwt_required
from ..models import CategoryAccess


@jwt_required
def set_access_user(data):
    name_exist = CategoryAccess.query.filter_by(name=data['name']).first()
    if name_exist:
        return {"message": "akses bernama {} sudah ada sebelumnya".format(data['name'])}, 400
    access_exist = CategoryAccess.query.filter(
        CategoryAccess.add_user == data['add_user'],
        CategoryAccess.delete_user == data['delete_user'],
        CategoryAccess.edit_user == data['edit_user'],
        CategoryAccess.add_job == data['add_job'],
        CategoryAccess.delete_job == data['delete_job'],
        CategoryAccess.update_job == data['update_job'],
        CategoryAccess.show_job == data['show_job'],
        CategoryAccess.print_job == data['print_job'],
        CategoryAccess.check_job == data['check_job'],
        CategoryAccess.service_job == data['service_job']
    ).first()
    if access_exist:
        return {"message": "kategori seperti ini sudah ada di {}".format(access_exist.name)}, 400
    category_access = CategoryAccess(
        name=data['name'],
        add_user=data['add_user'],
        delete_user=data['delete_user'],
        edit_user=data['edit_user'],
        add_job=data['add_job'],
        delete_job=data['delete_job'],
        update_job=data['update_job'],
        show_job=data['show_job'],
        print_job=data['print_job'],
        check_job=data['check_job'],
        service_job=data['service_job']
    )
    try:
        category_access.commit()
    except:
        return {"message": "error to save {}".format(data['name'])}, 400
    return {"message": "sukses menambah kategori {}".format(data['name'])}
