from db import ma
from models.part import Part


class PartSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Part
        include_fk = True
