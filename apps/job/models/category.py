from datetime import datetime
from core.database import db


class JobCategory(db.Model):
    __tablename__ = 'job_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    time_created = db.Column(db.DateTime, default=datetime.now())
    jobs = db.relationship('Job', lazy='subquery', backref='job_category')
