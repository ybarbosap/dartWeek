from werkzeug.security import generate_password_hash, check_password_hash

from myapp.ext.data_base import db


def password_hash(password):
    return generate_password_hash(password)


class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), unique=True)
    password = db.Column(db.String(128))
    transactions = db.relationship(
        'TransactionModel', backref='user', lazy=True)

    def autentication(self, password, login):
        return check_password_hash(self.password, password) and login == self.login
