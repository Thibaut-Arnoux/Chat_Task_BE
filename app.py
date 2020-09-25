from flask import Flask, json
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager, decode_token
from flask_restful import Api
from db import init_db, db
from routes.board import BoardAPI, BoardIdApi
from routes.part import PartAPI, PartIdApi
from routes.message import MessageAPI, MessageIdApi
from routes.user import UserApi, LoginApi
from models import *
from models.message import Message
from datetime import datetime

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('ENV_FILE_LOCATION')

    with app.app_context():
        init_db(app)
        socketio.init_app(app, cors_allowed_origins='*')

    jwt = JWTManager(app)
    api = Api(app)

    # Board endpoints
    api.add_resource(BoardAPI, '/api/board', endpoint='board')
    api.add_resource(BoardIdApi, '/api/board/<int:id>', endpoint='board_id')

    # Part endpoints
    api.add_resource(PartAPI, '/api/part', endpoint='part')
    api.add_resource(PartIdApi, '/api/part/<int:id>', endpoint='part_id')

    # Message endpoints
    api.add_resource(MessageAPI, '/api/message', endpoint='message')
    api.add_resource(MessageIdApi, '/api/message/<int:id>', endpoint='message_id')

    # User endpoints
    api.add_resource(UserApi, '/api/auth/signup', '/api/user', endpoint='user')
    api.add_resource(LoginApi, '/api/auth/login', endpoint='login')
    return app


@socketio.on('my_event')
def handle_my_custom_event(msg):
    info_token = decode_token(msg['access_token'])
    id = info_token['identity']

    msg.pop('access_token')
    msg['user_id'] = id
    msg['date'] = datetime.utcnow()
    db.session.add(Message(**msg))
    db.session.commit()
    socketio.emit('my_event',  json.dumps({'content': msg['content'], 'date': msg['date']}), broadcast=True)


if __name__ == '__main__':
    app = create_app()
    socketio.run(app)
