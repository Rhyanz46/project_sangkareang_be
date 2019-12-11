from flask_jwt_extended import jwt_required
from ..models import CategoryAccess
from apps.user.models import User


@jwt_required
def set_ca(data):
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


@jwt_required
def get_list_ca(name=None):
    if name:
        ca = CategoryAccess.query.filter_by(name=name).first()
        return ca.__serialize__()
    ca = CategoryAccess.query.all()
    result = []
    for a in ca:
        result.append(a.name)
    if len(result) < 0:
        return {"data": "empty"}, 402
    return {"data": result}


@jwt_required
def edit_ca(name, data):
    ca = CategoryAccess.query.filter_by(name=name).first()
    if not ca:
        return {"message": "{} is not found".format(name)}, 402
    if data['name'] != None:
        ca.name = data['name']
    if data['add_user'] != None:
        ca.add_user = data['add_user']
    if data['delete_user'] != None:
        ca.delete_user = data['delete_user']
    if data['edit_user'] != None:
        ca.edit_user = data['edit_user']
    if data['add_job'] != None:
        ca.add_job = data['add_job']
    if data['delete_job'] != None:
        ca.delete_job = data['delete_job']
    if data['update_job'] != None:
        ca.update_job = data['update_job']
    if data['show_job'] != None:
        ca.show_job = data['show_job']
    if data['print_job'] != None:
        ca.print_job = data['print_job']
    if data['check_job'] != None:
        ca.check_job = data['check_job']
    if data['service_job'] != None:
        ca.service_job = data['service_job']
    try:
        ca.commit()
    except:
        return {"message": "cant save"}, 500
    return {"message": "{} has been updated".format(name)}


@jwt_required
def set_user(ca_name, user_id, data):
    action = data['action']
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return {"message": "user with id : {} is not found".format(user_id)}, 402
    ca = CategoryAccess.query.filter_by(name=ca_name).first()
    if not ca:
        return {"message": "{} is not found".format(ca_name)}, 402
    if action == "on":
        try:
            ca.users.append(user)
            ca.commit()
        except:
            return {"message": "error to set {} to {}".format(user.username, ca_name)}, 500
        return {"message": "success to set {} to {}".format(user.username, ca_name)}
    elif action == "off":
        try:
            ca.users.remove(user)
            ca.commit()
        except:
            return {"message": "error to unset {} from {}".format(user.username, ca_name)}, 500
        return {"message": "success to unset {} from {}".format(user.username, ca_name)}

