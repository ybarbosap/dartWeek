from flask import Blueprint

from .routes import post, get_total, get_all
transaction = Blueprint('transaction', __name__, url_prefix='/transaction')
transaction.add_url_rule('/<int:id>', view_func=post, methods=['GET', 'POST'])
transaction.add_url_rule('/total/<string:anoMes>',
                         view_func=get_total, methods=['GET', ])
transaction.add_url_rule('/month/<string:anoMes>',
                         view_func=get_all, methods=['GET', ])


def init_app(app):
    app.register_blueprint(transaction)
