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


class SubJob(db.Model):
    __tablename__ = 'sub_job'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    name = db.Column(db.String(255))
    done = db.Column(db.Boolean, default=False)


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.TEXT)
    start_time = db.Column(db.Date, default=datetime.now())
    deadline = db.Column(db.Date)
    done = db.Column(db.Boolean, default=False)

    sub_job = db.relationship(SubJob, backref='job')
    history = db.relationship(JobHistory, backref='job')
    users = db.relationship('User', secondary=user_jobs, lazy='subquery', backref='job')

    time_created = db.Column(db.DateTime, default=datetime.now())

    def __serialize__(self):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_time": self.start_time,
            "deadline": self.deadline,
            "done": self.done
        }
        return data
