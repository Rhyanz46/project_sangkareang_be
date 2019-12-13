from datetime import datetime
from core.database import db


user_jobs = db.Table('user_jobs',
                      db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))


class JobHistory(db.Model):
    __tablename__ = 'job_history'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    user_detail_id = db.Column(db.Integer, db.ForeignKey('user_detail.id'))
    name = db.Column(db.String(255))
    time_created = db.Column(db.DateTime, default=datetime.now())


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.TEXT)
    start_time = db.Column(db.SmallInteger)
    deadline = db.Column(db.SmallInteger)
    status = db.Column(db.SmallInteger)

    users = db.relationship(
        'User',
        secondary=user_jobs,
        lazy='subquery',
        backref='job')

    history = db.relationship(JobHistory, uselist=False, backref='job')
