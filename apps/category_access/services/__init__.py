from flask_jwt_extended import jwt_required
from ..models import CategoryAccess


@jwt_required
def set_access_user(data):
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
    category_access.commit()
    return {"message": "sukses menambah kategori {}".format(data['name'])}
