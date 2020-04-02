from datetime import datetime

from flask import jsonify, request

from myapp.models.transaction_model import TransactionModel
from myapp.models.category_model import Options, CategoryModel
from myapp.models.user_model import UserModel
from myapp.ext.data_base import db
from myapp.authenticate import jwt_required


@jwt_required
def get_all(current_user, anoMes):
    anoMes = anoMes.split('-')
    dateFormat = "%Y/%m/%d"
    dateIstr = f'{anoMes[0]}/{anoMes[1]}/01'

    try:
        dateFstr = f'{anoMes[0]}/{anoMes[1]}/31'
    except ValueError as e:
        pass
    finally:
        dateFstr = f'{anoMes[0]}/{int(anoMes[1])+1}/30'

    dateI = datetime.strptime(dateIstr, dateFormat)
    dateF = datetime.strptime(dateFstr, dateFormat)

    try:
        transactions = db.session.query(TransactionModel).\
            filter(TransactionModel.user_id == current_user.id)

        def filterFunc(t):
            if t.date.month <= dateF.month and t.date.month >= dateI.month:
                return t

        transactions_filter = []
        for e in transactions:
            if(filterFunc(e) != None):
                transactions_filter.append(e)

        response = jsonify([trans.fromJson() for trans in transactions_filter])

        return response, 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Fail"})


@jwt_required
def get_total(current_user, anoMes):
    anoMes = anoMes.split('-')
    dateFormat = "%Y/%m"
    dateStr = f'{anoMes[0]}/{anoMes[1]}'
    date = datetime.strptime(dateStr, dateFormat)

    try:
        transactions = TransactionModel.query.filter_by(
            user_id=current_user.id).all()

        def filterFunc(t):
            if t.date.month == date.month and t.date.year == date.year:
                return t

        transactions_filter = []
        for e in transactions:
            if(filterFunc(e) != None):
                transactions_filter.append(e)

        incomes = 0
        expenses = 0
        total = 0
        for e in transactions_filter:
            if(e.category.categoryType.name == Options.expense.name):
                expenses += e.value
            if(e.category.categoryType.name == Options.income.name):
                incomes = + e.value
            total += e.value

        response = jsonify({'expenses': expenses, 'incomes': incomes,
                            'total': total, "balance": total - expenses})

        return response, 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Fail"})


@jwt_required
def post(current_user, id):
    data = request.get_json()
    category = CategoryModel.query.filter_by(id=id).first()

    try:
        transaction = TransactionModel(value=data['value'], user=current_user,
                                       description=data['description'], category=category)

        if "date" in data:
            transaction.date = datetime.strptime(data['date'], "%Y/%m/%d")

        db.session.add(transaction)
        db.session.commit()

        response = jsonify(transaction.fromJson())

        return response, 200

    except Exception as e:
        print(e)
        response = jsonify({'message': "Falha"})

        return response


@jwt_required
def put(id, current_user):
    data = request.get_json()
    try:
        transaction = TransactionModel.query.filter_by(id=id).first()
        transaction.value = data['value']
        transaction.description = data['description']

        db.session.add(transaction)
        db.session.commit()

        response = jsonify(
            transaction.fromJson()
        )

        return response, 200
    except Exception as e:
        pass
