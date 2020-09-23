from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api
from db import init_db
from routes.board import BoardAPI, BoardIdApi
from models import *


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('ENV_FILE_LOCATION')

    with app.app_context():
        init_db(app)
    api = Api(app)

    # Board endpoint
    api.add_resource(BoardAPI, '/api/board', endpoint='board')
    api.add_resource(BoardIdApi, '/api/board/<int:id>', endpoint='board_id')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
