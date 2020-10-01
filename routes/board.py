from flask import request, Response, json
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models.board import Board
from schemas.board import BoardSchema
from db import db


class BoardAPI(Resource):

    @jwt_required
    def get(self):
        try:
            boards = Board.query.all()
            board_schema = BoardSchema(many=True)
            output = board_schema.dump(boards)
            return Response(json.dumps({'boards': output}), mimetype="application/json", status=200)
        except Exception:
            raise

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            board = Board(**body)
            db.session.add(board)
            db.session.commit()
            return Response(json.dumps({'id': board.id}), mimetype="application/json", status=200)
        except Exception:
            raise


class BoardIdApi(Resource):

    @jwt_required
    def get(self, id):
        try:
            board = Board.query.get_or_404(id)
            board_schema = BoardSchema()
            output = board_schema.dump(board)
            return Response(json.dumps(output), mimetype="application/json", status=200)
        except Exception:
            raise

    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            board = Board.query.get(id)
            board_schema = BoardSchema()
            for key, value in body.items():
                setattr(board, key, value)
            db.session.commit()
            output = board_schema.dump(board)
            return Response(json.dumps(output), mimetype="application/json", status=200)
        except Exception:
            raise

    @jwt_required
    def delete(self, id):
        try:
            board = Board.query.get(id)
            db.session.delete(board)
            db.session.commit()
            return Response('', status=204)
        except Exception:
            raise


class BoardIdPartsApi(Resource):
    @jwt_required
    def get(self, id):
        try:
            board = Board.query.get_or_404(id)
            board_schema = BoardSchema()
            output = board_schema.dump(board)
            output['parts'] = []
            for part in board.parts:
                msgs = []

                # Add msg of part
                for msg in part.messages:
                    msgs.append(msg.content)

                # Create output with Part and Msg informations
                output['parts'].append({
                    'id': part.id,
                    'name': part.name,
                    'tag': part.tag,
                    'msgs': msgs
                })
            return Response(json.dumps(output), mimetype="application/json", status=200)
        except Exception:
            raise
