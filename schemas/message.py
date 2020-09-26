from db import ma
from models.message import Message


class MessageSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Message
        include_fk = True
