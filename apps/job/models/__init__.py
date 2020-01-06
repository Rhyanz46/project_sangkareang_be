from datetime import datetime
from core.database import db

from .history import JobHistory
from .sub import SubJob
from .category import JobCategory

user_jobs = db.Table('user_jobs',
                      db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.TEXT)
    start_time = db.Column(db.Date, default=datetime.now())
    deadline = db.Column(db.Date)
    done = db.Column(db.Boolean, default=False)
    accept = db.Column(db.Boolean, default=False)

    nilai_material = db.Column(db.String(255))
    nilai_jasa = db.Column(db.String(255))

    job_location = db.Column(db.String(255))
    no_spk = db.Column(db.String(255))
    given_by = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey("job_category.id"))

    sub_job = db.relationship(SubJob, backref='job')
    history = db.relationship(JobHistory, backref='job')
    users = db.relationship('User', secondary=user_jobs, lazy='subquery', backref='job')

    time_created = db.Column(db.DateTime, default=datetime.now())

    def __serialize__(self):
        job_ca = JobCategory.query.filter_by(id=self.category_id).first()
        job_ca_name = None
        if job_ca:
            job_ca_name = job_ca.name
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_time": self.start_time,
            "deadline": self.deadline,
            "done": self.done,
            "given_by": self.given_by,
            "job_location": self.job_location,
            "no_spk": self.no_spk,
            "nilai": {
                "material": self.nilai_material,
                "jasa": self.nilai_jasa
            },
            "category": {
                "id": self.category_id,
                "name": job_ca_name
            }
        }
        return data
