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
    return '<h1>Backend</h1>'

@app.route('/users', methods=['POST'])
def users():
    username = request.get_json()('username'),
    email = request.get_json()('email'),
    password = request.get_json()('password')

    #  = Product(name=name, price=price, image=image)
    #     db.session.add(product)
    #     db.session.commit()
    #     response = make_response(jsonify({'message': 'Product added successfully'}), 201)


    data=request.json
    print(data)
    return jsonify(data)


# TRYING TO GET THE NEW PRODUCT POST WORKING
# @app.route('/add_product', methods = ['POST'])
# def add_product():
#     data = request.json
#     return jsonify(data)

@app.route('/category_products', methods=['POST'])
def add_product():

    new_product = Product(
        name = request.get_json()['name'],    
        price = request.get_json()['price'],
        image = request.get_json()['image']
    )
        # product = Product(name=name, price=price, image=image)
    db.session.add(new_product)
    db.session.commit()
    
    response = make_response(jsonify(new_product), 201)

    return response

# route for users from registration
# users = []

# @app.route('/users', methods=['POST'])
# def register_user():
#     data = request.json
#     username = data['username']
#     password = data['password']

#     # adding new user

# @app.route('/users', methods=['POST'])
# def create_user():

#     username = request.json['username']
#     password = request.json['password']


#     if User.query.filter_by(username=username).first():
#         return jsonify({'error': 'User already exists'}), 400
    

#     user = User(username=username, password=generate_password_hash(password))
#     db.session.add(user)
#     db.session.commit()


#     response = {
#         'id': user.id,
#         'username': user.username
#     }
#     return jsonify(response), 201


    

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
