from ..models import User
from core import result


def register(data):
    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    user.add()
    return result({'data': 'success register'}, 200)
