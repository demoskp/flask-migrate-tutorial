from flask import request, jsonify
from flask_restful import Resource, abort

from extensions import db
from models.users import User


class UserList(Resource):
    def get(self):
        users = User.query.all()
        return jsonify(results=users)

    def post(self):
        data = request.json

        user = User(
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email"),
        )

        db.session.add(user)
        db.session.commit()

        return jsonify(msg="User created", user=user)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)

        return jsonify(user=user)

    def put(self, user_id):
        data = request.json

        user = User.query.get_or_404(user_id)
        user.age = data.get("age")
        user.name = data.get("name")

        db.session.commit()

        return jsonify(msg="User updated", user=user)

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return jsonify(msg="User deleted")
