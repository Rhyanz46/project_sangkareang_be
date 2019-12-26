from core.database import db


class SubJob(db.Model):
    __tablename__ = 'sub_job'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    name = db.Column(db.String(255))
    done = db.Column(db.Boolean, default=False)
