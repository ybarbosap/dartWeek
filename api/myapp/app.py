from flask import Flask

from myapp.ext import data_base
from myapp.blueprints import user
from myapp.blueprints import category
from myapp.blueprints import transaction


def create_app():
    app = Flask(__name__)
    DEBUG = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '123asdf'

    data_base.init_app(app)

    user.init_app(app)
    category.init_app(app)
    transaction.init_app(app)

    return app
# 'postgresql://postgres:07121994#@localhost/dartweek'
