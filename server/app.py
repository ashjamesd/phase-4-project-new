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

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.json.get('name')
    price = request.json.get('price')
    image = request.json.get('image')

    if not all([name, price, image]):
        response = make_response(jsonify({'error': 'Missing required parameters'}), 400)
    else:
        product = Product(name=name, price=price, image=image)
        db.session.add(product)
        db.session.commit()
        response = make_response(jsonify({'message': 'Product added successfully'}), 201)

    return response

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

@app.route('/category_products', methods=['GET', 'POST', 'DELETE'])
def category_products():
    if request.method == 'GET':
        # Handle GET request to retrieve all category products
        category_products = CategoryProduct.query.all()
        category_products_dict = [category_product.to_dict() for category_product in category_products]
        response = make_response(jsonify(category_products_dict), 200)

    elif request.method == 'POST':
        # Handle POST request to add a new category product
        product_id = request.json.get('product_id')
        category_id = request.json.get('category_id')
        category_product = CategoryProduct(product_id=product_id, category_id=category_id)
        db.session.add(category_product)
        db.session.commit()
        response = make_response(jsonify({'message': 'Category product added'}), 201)

    elif request.method == 'DELETE':
        # Handle DELETE request to remove a category product
        category_product_id = request.args.get('id')
        category_product = CategoryProduct.query.filter_by(id=category_product_id).first()

        if category_product:
            db.session.delete(category_product)
            db.session.commit()
            response = make_response(jsonify({'message': 'Category product deleted'}), 200)
        else:
            response = make_response(jsonify({'error': 'Category product not found'}), 404)

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
