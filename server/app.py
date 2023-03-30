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
