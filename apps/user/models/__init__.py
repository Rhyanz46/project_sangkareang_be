from datetime import datetime
from core.database import db
from apps.job.models import JobHistory


class UserDetail(db.Model):
    __tablename__ = 'user_detail'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fullname = db.Column(db.String(90))
    address = db.Column(db.TEXT)
    phone_number = db.Column(db.BigInteger, unique=True)
    work_start_time = db.Column(db.Date, default=datetime.now())
    activate = db.Column(db.Boolean, default=True)
    created_time = db.Column(db.DateTime, default=datetime.now())

    job_history = db.relationship(JobHistory, backref='user_detail')

    def __serialize__(self, id=None):
        if not id:
            return {
                "id": self.id,
                "user_id": self.user_id,
                "fullname": self.fullname,
                "address": self.address,
                "phone_number": self.phone_number,
                "work_start_time": self.work_start_time,
                "activate": self.activate,
                "created_time": self.created_time
            }
        user = UserDetail.query.get(id)
        if not user:
            return None
        return {
            "id": user.id,
            "user_id": user.user_id,
            "fullname": user.fullname,
            "address": user.address,
            "phone_number": user.phone_number,
            "work_start_time": user.work_start_time,
            "activate": user.activate,
            "created_time": user.created_time
        }


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    category_access_id = db.Column(db.Integer, db.ForeignKey('category_access.id'), nullable=True)
    username = db.Column(db.String(90), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    user_detail = db.relationship(UserDetail, uselist=False, backref='user')

    def __serialize__(self, detail=False):
        data = {
            "id": self.id,
            "category_access_id": self.category_access_id,
            "username": self.username,
            "email": self.email
        }
        if detail:
            data.update({"user_detail": UserDetail().__serialize__(id=self.id)})
        return data
