from db import ma
from models import Board
# from models.part import PartSchema


class BoardSchema(ma.SQLAlchemyAutoSchema):
    # If we wanna add relationship in serialize representation
    # parts = ma.Nested(PartSchema, many=True)

    class Meta:
        model = Board
