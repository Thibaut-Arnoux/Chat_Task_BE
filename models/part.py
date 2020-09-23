from db import db


class Part(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    messages = db.relationship('Message', backref='part')
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
