from datetime import datetime
from db import db, ma


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'))


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
