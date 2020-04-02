from functools import wraps

import jwt

from flask import request, jsonify, current_app

from myapp.models.user_model import UserModel


def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        token = None

        if "authorization" in request.headers:
            token = request.headers['authorization']

        if not token:
            return jsonify({"error": "You don't have permission"}), 403

        if not "Bearer" in token:
            return({"error": "Invalid token"}), 401

        try:
            token_pure = token.replace("Bearer", "")
            decoded = jwt.decode(token_pure, current_app.config['SECRET_KEY'])
            current_user = UserModel.query.get(decoded['id'])
        except:
            return jsonify({"error": "expired token"})

        return func(current_user=current_user, *args, **kwargs)
    return wrapper
