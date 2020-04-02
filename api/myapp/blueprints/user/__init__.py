from flask import Blueprint

from .routes import post_user, login

user = Blueprint('user', __name__, url_prefix='/user')
user.add_url_rule('/create', view_func=post_user, methods=['GET', 'POST'])
user.add_url_rule('/login', view_func=login, methods=['POST'])


def init_app(app):
    app.register_blueprint(user)
