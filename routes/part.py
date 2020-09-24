from flask import request, Response, json
from flask_restful import Resource
from models.part import Part, PartSchema
from db import db


class PartAPI(Resource):

    def get(self):
        try:
            parts = Part.query.all()
            part_schema = PartSchema(many=True)
            output = part_schema.dump(parts)
            return Response(json.dumps({'parts': output}), mimetype="application/json", status=200)
        except Exception:
            raise

    def post(self):
        try:
            body = request.get_json()
            part = Part(**body)
            db.session.add(part)
            db.session.commit()
            return Response(json.dumps({'id': part.id}), mimetype="application/json", status=200)
        except Exception:
            raise


class PartIdApi(Resource):

    def get(self, id):
        try:
            part = Part.query.get(id)
            part_schema = PartSchema()
            output = part_schema.dump(part)
            return Response(json.dumps(output), mimetype="application/json", status=200)
        except Exception:
            raise

    def put(self, id):
        try:
            body = request.get_json()
            part = Part.query.get(id)
            part_schema = PartSchema()
            for key, value in body.items():
                setattr(part, key, value)
            db.session.commit()
            output = part_schema.dump(part)
            return Response(json.dumps(output), mimetype="application/json", status=200)
        except Exception:
            raise

    def delete(self, id):
        try:
            part = Part.query.get(id)
            db.session.delete(part)
            db.session.commit()
            return Response('', status=204)
        except Exception:
            raise
