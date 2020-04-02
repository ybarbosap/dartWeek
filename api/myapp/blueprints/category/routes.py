import signal

from flask import request, jsonify

from myapp.models.category_model import CategoryModel, Options
from myapp.ext.data_base import db
from myapp.authenticate import jwt_required


@jwt_required
def get_all_type(typeCategory, current_user):

    if(typeCategory == Options.expense.value):
        category = CategoryModel.query.filter_by(
            categoryType=Options.expense).all()

    if(typeCategory == Options.income.value):
        category = CategoryModel.query.filter_by(
            categoryType=Options.income).all()

    response = jsonify([{"id": c.id, "nome": c.nane} for c in category])

    return response, 200


@jwt_required
def post(current_user):
    data = request.get_json()

    if(data['category'] == Options.expense.name):
        category = data['category']
    elif(data['category'] == Options.income.name):
        category = data['category']
    else:
        return jsonify({'error': "category not found"}), 404

    try:
        c = CategoryModel(nane=data['name'], categoryType=category)

        db.session.add(c)
        db.session.commit()

        response = jsonify({'id': c.id, 'name': c.nane,
                            "category": c.categoryType.name})

        return response, 201
    except Exception as e:
        print(e)
        return jsonify({'error': 'Fail'})


@jwt_required
def delete(current_user, id):
    try:
        c = CategoryModel.query.filter_by(id=id).first()
        category = c.nane

        db.session.delete(c)
        db.session.commit()

        response = jsonify({"deleted": category})

        return response, 200

    except Exception as e:
        print(e)
        return jsonify({"error": "Fail"}), 404
