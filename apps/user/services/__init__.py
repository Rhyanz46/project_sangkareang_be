from flask_jwt_extended import create_access_token, jwt_required
from ..models import User, UserDetail


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
    user.add()
    token = create_access_token(identity=user.id)
    return {'token': token}, 200


def login(data):
    username = data['username']
    password = data['password']
    user = User.query.filter(User.username == username, User.password == password).first()
    if user:
        token = create_access_token(identity=user.id)
        return {'token': token}, 200
    return {'data': 'username atau password salah'}, 403

