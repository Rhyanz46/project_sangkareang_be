from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from ..models import User, UserDetail


def store_data_user(data):
    detail = UserDetail(
        fullname=data['fullname'],
        address=data['address'],
        phone_number=data['phone_number'],
        work_start_time=data['work_start_time'],
        activate=data['activate'],
    )

    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        user_detail=detail
    )
    # try:
    user.commit()
    return user
    # except:
    #     return None


def register(data):
    username_exist = User.query.filter_by(username=data['username']).first()
    email_exist = User.query.filter_by(email=data['email']).first()
    phone_exist = UserDetail.query.filter_by(phone_number=data['phone_number']).first()
    if username_exist:
        return {'message': 'username is exist'}, 400
    elif email_exist:
        return {'message': 'email is exist'}, 400
    elif phone_exist:
        return {'message': 'phone_number is already used'}, 400

    saved = store_data_user(data)
    if not saved:
        return {'error': 'failed to save data'}, 402
    token = create_access_token(identity=saved.id)
    return {'token': token}, 200


def login(data):
    username = data['username']
    password = data['password']
    user = User.query.filter(User.username == username, User.password == password).first()
    if user:
        token = create_access_token(identity=user.id)
        return {'token': token}, 200
    return {'data': 'username atau password salah'}, 403


@jwt_required
def update(username, data):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'error': 'user is not found'}, 402

    if data['username']:
        user.username = data['username']
    if data['email']:
        user.email = data['email']
    if data['fullname']:
        user.fullname = data['fullname']
    if data['address']:
        user.address = data['address']
    if data['phone_number']:
        user.phone_number = data['phone_number']
    if data['work_start_time']:
        user.work_start_time = data['work_start_time']
    if data['activate']:
        user.activate = data['activate']
    if data['password']:
        user.password = data['password']

    try:
        user.commit()
    except:
        return {'error': 'something wrong'}, 402
    return {'token': "edited"}, 200


def show_user_detail(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'error': 'user is not found'}, 402
    return user.__serialize__(detail=True), 200
