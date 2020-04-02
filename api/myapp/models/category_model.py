from enum import Enum

from myapp.ext.data_base import db


class Options(Enum):
    expense = 0
    income = 1


class CategoryModel(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer(), primary_key=True)
    nane = db.Column(db.String())
    categoryType = db.Column(db.Enum(Options))
    transactions = db.relationship('TransactionModel', backref='category', lazy=True)
