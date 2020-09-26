from db import db


class Board(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    nb_part = db.Column(db.Integer, nullable=False)
    parts = db.relationship('Part', cascade="all, delete", backref='board')
    messages = db.relationship('Message', cascade="all, delete", backref='board')
