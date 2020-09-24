from db import db, ma


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    messages = db.relationship('Message', cascade="all, delete", backref='user')


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
