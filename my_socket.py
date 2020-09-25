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

    msg.pop('access_token')
    msg['user_id'] = id
    msg['date'] = datetime.utcnow()
    db.session.add(Message(**msg))
    db.session.commit()
    socket.emit('my_event',  json.dumps({'content': msg['content'], 'date': msg['date']}), broadcast=True)
