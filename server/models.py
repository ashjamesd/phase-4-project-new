from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

from config import db

db = SQLAlchemy()

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    images = db.Column(db.String)
    weight = db.Column(db.Float)
    description = db.Column(db.Integer)
    thumbnail = db.Column(db.String)
    category = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    in_stock = db.Column(db.Boolean)

class ProductCategory(db.Model, SerializerMixin):
    __tablename__ = 'product_categories'

    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    name = db.Column(db.String)

class Color(db.Model, SerializerMixin):
    __tablename__ = 'colors'

    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    color = db.Column(db.String)