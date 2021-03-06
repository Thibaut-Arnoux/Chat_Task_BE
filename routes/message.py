from flask import request, Response, json
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models.message import Message
from schemas.message import MessageSchema
from db import db


class MessageAPI(Resource):

    @jwt_required
    def get(self):
        try:
            messages = Message.query.all()
            msg_schema = MessageSchema(many=True)
            output = msg_schema.dump(messages)
            return Response(json.dumps({'messages': output}), mimetype="application/json", status=200)
        except Exception:
            raise

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            msg = Message(**body)
            db.session.add(msg)
            db.session.commit()
            return Response(json.dumps({'id': msg.id}), mimetype="application/json", status=200)
        except Exception:
            raise


class MessageIdApi(Resource):

    @jwt_required
    def get(self, id):
        try:
            msg = Message.query.get(id)
            msg_schema = MessageSchema()
            output = msg_schema.dump(msg)
            return Response(json.dumps(output), mimetype="application/json", status=200)
        except Exception:
            raise

    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            msg = Message.query.get(id)
            msg_schema = MessageSchema()
            for key, value in body.items():
                setattr(msg, key, value)
            db.session.commit()
            output = msg_schema.dump(msg)
            return Response(json.dumps(output), mimetype="application/json", status=200)
        except Exception:
            raise

    @jwt_required
    def delete(self, id):
        try:
            msg = Message.query.get(id)
            db.session.delete(msg)
            db.session.commit()
            return Response('', status=204)
        except Exception:
            raise
