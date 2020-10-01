from flask import json
from flask_socketio import SocketIO
from flask_jwt_extended import decode_token
from models.message import Message
from datetime import datetime
from db import db


socket = SocketIO()


def init_socket(app):
    socket.init_app(app, cors_allowed_origins='*')


@socket.on('my_event')
def handle_my_custom_event(msg):
    info_token = decode_token(msg['access_token'])
    id = info_token['identity']

    msg_db = Message(content=msg['content'], user_id=id, board_id=msg['board_id'])
    tag = msg_db.set_part_id()
    db.session.add(msg_db)
    db.session.commit()
    socket.emit('my_event',  json.dumps({'content': msg_db.content, 'date': msg_db.date, 'tag': tag}), broadcast=True)
