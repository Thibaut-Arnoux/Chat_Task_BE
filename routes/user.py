from flask import request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask_restful import Resource
from models.user import User, UserSchema
from db import db
import datetime


class LoginApi(Resource):

    def post(self):
        try:
            body = request.get_json()
            user = User.query.filter_by(name=body.get('name')).first()
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)

            return Response(json.dumps({'access_token': access_token}), mimetype="application/json", status=200)
        except Exception:
            raise


class UserApi(Resource):

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            db.session.add(user)
            db.session.commit()
            return Response(json.dumps({'id': user.id}), mimetype="application/json", status=200)
        except Exception:
            raise

