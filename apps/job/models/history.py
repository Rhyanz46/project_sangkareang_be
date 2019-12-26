from datetime import datetime
from core.database import db


class JobHistory(db.Model):
    __tablename__ = 'job_history'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    user_detail_id = db.Column(db.Integer, db.ForeignKey('user_detail.id'))
    name = db.Column(db.String(255))
    time_created = db.Column(db.DateTime, default=datetime.now())
