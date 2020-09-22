from db import db


class Board(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    nb_part = db.Column(db.Integer, nullable=False)
    parts = db.relationship('Part', backref='board')

    def __repr__(self):
        return f'{self.name} with {self.nb_part} part(s).'
