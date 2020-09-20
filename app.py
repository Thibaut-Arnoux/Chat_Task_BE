from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api
from db import init_db
from models import *


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('ENV_FILE_LOCATION')

    api = Api(app)
    with app.app_context():
        init_db(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
