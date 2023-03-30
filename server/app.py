#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate


# Local imports
from models import db, Product, Category, CategoryProduct

# Views go here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Products</h1>'


# TRYING TO GET THE NEW PRODUCT POST WORKING
# @app.route('/add_product', methods = ['POST'])
# def add_product():
#     data = request.json
#     return jsonify(data)

# route for users from registration
users = []

@app.route('/users', methods=['POST'])
def register_user():
    data = request.json
    username = data['username']
    password = data['password']

    # adding new user
    user = {'username': username, 'password': password}
    users.append(user)

    return response

@app.route('/category_products', methods = ['POST'])
def categoryProducts():
    try:

        new_category_product = CategoryProduct(
            product_id = request.get_json()['product_id'],
            category_id = request.get_json()['category_id']
        )

        db.session.add(new_category_product)
        db.session.commit()

        associated_product = Product.query.filter(Product.id == new_category_product.product_id).first()
        associated_product_dict = associated_product.to_dict()

        response = make_response(
            jsonify(associated_product_dict),
            201
        )

    except ValueError:

        response = make_response(
            { "errors": ["validation errors"] },
            400
        )

    return response

@app.route('/products', methods = ['GET'])
def products():
    products = Product.query.all()
    products_dict = [product.to_dict() for product in products]

    response = make_response(
        jsonify(products_dict),
        200
    )

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)



#test update
