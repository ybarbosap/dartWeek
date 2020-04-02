from werkzeug.security import generate_password_hash
from flask import jsonify, request, current_app

from myapp.models.user_model import UserModel
from myapp.ext.data_base import db
from myapp import app

import datetime
import jwt


def post_user():
    data = request.get_json()
    user = UserModel(login=data['login'],
                     password=generate_password_hash(data['password']))

    db.session.add(user)
    db.session.commit()

    response = jsonify({'user': user.login, 'create': 'ok'})

    return response, 200


def login():
    data = request.get_json()
    user = UserModel.query.filter_by(login=data['login']).first()

    try:
        validate = user.autentication(password=data['password'],
                                      login=data['login'])

        if not validate:
            return jsonify({"error": "invalid credentials"})

        payload = {"id": user.id,
                   "exp": datetime.datetime.utcnow() + datetime.timedelta(days=365)}

        token = jwt.encode(payload, current_app.config['SECRET_KEY'])

        return jsonify({"validate": validate,
                        "token": f"Bearer{token.decode('utf-8')}"}), 200

    except Exception as e:
        print(e)

        return jsonify({"message": "User not found"}), 404
