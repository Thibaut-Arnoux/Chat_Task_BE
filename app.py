from flask import Flask, json
from flask_socketio import SocketIO, send
from flask_restful import Api
from db import init_db, db
from routes.board import BoardAPI, BoardIdApi
from routes.part import PartAPI, PartIdApi
from models import *
from models.message import Message
from datetime import datetime



socketio = SocketIO()
print("SocketIO")

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('ENV_FILE_LOCATION')

    with app.app_context():
        init_db(app)
        socketio.init_app(app, cors_allowed_origins='*')
    api = Api(app)

    # Board endpoints
    api.add_resource(BoardAPI, '/api/board', endpoint='board')
    api.add_resource(BoardIdApi, '/api/board/<int:id>', endpoint='board_id')

    # Part endpoints
    api.add_resource(PartAPI, '/api/part', endpoint='part')
    api.add_resource(PartIdApi, '/api/part/<int:id>', endpoint='part_id')

    return app





@socketio.on('my_event')
def handle_my_custom_event(msg):
    print(f"{type(msg)} : {msg}")
    msg['date'] = datetime.utcnow()
    print(msg['date'])
    db.session.add(Message(**msg))
    db.session.commit()
    socketio.emit('my_event',  json.dumps({'content' : msg['content'], 'date' : msg['date']}), broadcast=True)








if __name__ == '__main__':
    app = create_app()
    socketio.run(app)



