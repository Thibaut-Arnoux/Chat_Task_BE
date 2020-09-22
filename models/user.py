from db import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    messages = db.relationship('Message', backref='user')

    def __repr__(self):
        return f'{self.name}.'
