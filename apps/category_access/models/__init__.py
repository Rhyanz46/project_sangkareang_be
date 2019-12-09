from core.database import db
from apps.user.models import UserDetail


class CategoryAccess(db.Model):
    __tablename__ = 'category_access'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    add_job = db.Column(db.Boolean, default=True)
    delete_job = db.Column(db.Boolean, default=False)
    update_job = db.Column(db.Boolean, default=False)
    show_job = db.Column(db.Boolean, default=True)
    print_job = db.Column(db.Boolean, default=True)
    check_job = db.Column(db.Boolean, default=True)
    service_job = db.Column(db.Boolean, default=True)

    users = db.relationship(UserDetail, backref='category_access')
