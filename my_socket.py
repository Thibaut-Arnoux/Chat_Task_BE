from flask import json
from flask_socketio import SocketIO, join_room, leave_room
from flask_jwt_extended import decode_token
from models.message import Message
from models.user import User
from db import db


socket = SocketIO()


def init_socket(app):
    socket.init_app(app, cors_allowed_origins='*')


@socket.on('join')
def on_join(msg):
    room = msg['board_id']
    join_room(room)


@socket.on('leave')
def on_leave(msg):
    room = msg['board_id']
    leave_room(room)


@socket.on('my_event')
def handle_my_custom_event(msg):
    info_token = decode_token(msg['access_token'])
    id = info_token['identity']

    user = User.query.get(id)
    msg_db = Message(content=msg['content'], user_id=user.id, board_id=msg['board_id'])
    tag = msg_db.set_part_id()
    db.session.add(msg_db)
    db.session.commit()

    room = msg['board_id']
    socket.emit('my_event',  json.dumps(
        {'user': user.name,
         'content': msg_db.content,
         'date': msg_db.date,
         'tag': tag}), room=room)  # broadcast=True
