from datetime import datetime
from core.database import db
from apps.job.models import JobHistory


class UserDetail(db.Model):
    __tablename__ = 'user_detail'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fullname = db.Column(db.String(90))
    address = db.Column(db.TEXT)
    phone_number = db.Column(db.BigInteger)
    work_start_time = db.Column(db.DateTime, default=datetime.now())
    activate = db.Column(db.Boolean, default=True)
    join_time = db.Column(db.TEXT)
    created_time = db.Column(db.DateTime, default=datetime.now())

    job_history = db.relationship(JobHistory, backref='user_detail')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    category_access_id = db.Column(db.Integer, db.ForeignKey('category_access.id'))
    username = db.Column(db.String(90), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    user_detail = db.relationship(UserDetail, uselist=False, backref='user')


