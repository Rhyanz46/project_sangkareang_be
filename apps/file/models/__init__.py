from core.database import db


class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    link = db.Column(db.TEXT)
    type = db.Column(db.SmallInteger)
