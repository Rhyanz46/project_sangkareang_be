from core.database import db
from apps.post.models import Post


class UserDetail(db.Model):
    __tablename__ = 'user_detail'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    desc = db.Column(db.TEXT)
    photo = db.Column(db.TEXT)
    linkedin = db.Column(db.TEXT)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(90), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    level = db.Column(db.SMALLINT, nullable=False, default=0)

    user_detail = db.relationship(UserDetail, uselist=False, backref='user')
    posts = db.relationship(Post, uselist=False, backref='user')


