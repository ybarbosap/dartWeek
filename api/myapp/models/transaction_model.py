import datetime

from myapp.ext.data_base import db
from myapp.models.user_model import UserModel
from myapp.models.category_model import CategoryModel


class TransactionModel(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer(), primary_key=True)

    value = db.Column(db.Float(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer(), db.ForeignKey('categorys.id'))
    description = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime, index=True,
                     default=datetime.datetime.utcnow().date())

    def fromJson(self):
        response = {
            "id": self.id,
            "user": self.user.login,
            "value": self.value,
            "description": self.description,
            "date": self.date.strftime('%d/%m/%Y'),
            "category": {
                "id": self.category.id,
                "name": self.category.nane,
                "type": self.category.categoryType.name,
            }
        }
        return response
