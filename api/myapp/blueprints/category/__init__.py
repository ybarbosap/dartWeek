from flask import Blueprint
from .routes import get_all_type, post, delete

category = Blueprint('category', __name__, url_prefix='/category')
category.add_url_rule('/', view_func=post, methods=['POST'])
category.add_url_rule('/dell/<int:id>', view_func=delete)
category.add_url_rule('/<int:typeCategory>', view_func=get_all_type)


def init_app(app):
    app.register_blueprint(category)
