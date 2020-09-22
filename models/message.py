from datetime import datetime
from db import db


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'))

    def __repr__(self):
        return f'{self.content} by user id {self.user_id} in column {self.part_id}.'
