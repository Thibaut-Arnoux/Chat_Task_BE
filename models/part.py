from db import db, ma


class Part(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    messages = db.relationship('Message', backref='part')


class PartSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Part
        include_fk = True
