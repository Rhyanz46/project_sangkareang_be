from core.database import db
from apps.comment.models import Comment
from apps.category.models import Category, category_tag


class PageType(db.Model):
    __tablename__ = 'page_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), unique=True)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    page_type = db.Column(db.Integer, db.ForeignKey('page_type.id'))
    writer = db.Column(db.Integer, db.ForeignKey('user_detail.id'))
    content = db.Column(db.TEXT)
    status = db.Column(db.SmallInteger)

    categories = db.relationship(Category, secondary=category_tag, backref='post')
    comments = db.relationship(Comment, backref='post', lazy=True)
