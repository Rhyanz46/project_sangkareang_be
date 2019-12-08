from flask_sqlalchemy import SQLAlchemy, Model


class Database(Model):
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


db = SQLAlchemy(model_class=Database)
