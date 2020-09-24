from db import db, ma
# from models.part import PartSchema


class Board(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    nb_part = db.Column(db.Integer, nullable=False)
    parts = db.relationship('Part', cascade="all, delete", backref='board')
    messages = db.relationship('Message', cascade="all, delete", backref='board')


class BoardSchema(ma.SQLAlchemyAutoSchema):
    # If we wanna add relationship in serialize representation
    # parts = ma.Nested(PartSchema, many=True)

    class Meta:
        model = Board
