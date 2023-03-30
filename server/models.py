# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin

# from config import db

# db = SQLAlchemy()

# class Product(db.Model, SerializerMixin):
#     __tablename__ = 'products'

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     price = db.Column(db.Float)
#     image = db.Column(db.String)
#     # weight = db.Column(db.Float)
#     # description = db.Column(db.Integer)
#     # thumbnail = db.Column(db.String)
#     category = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default = db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate = db.func.now())
#     # in_stock = db.Column(db.Boolean)

#     product_categories = db.relationship('ProductCategory', backref='product')
#     color = db.relationship('ProductCategory', backref='color')

# class ProductCategory(db.Model, SerializerMixin):
#     __tablename__ = 'product_categories'

#     id = db.Column(db.Integer, primary_key = True)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     name = db.Column(db.String)


# class Color(db.Model, SerializerMixin):
#     __tablename__ = 'colors'

#     id = db.Column(db.Integer, primary_key = True)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     color = db.Column(db.String)

# class OrderDetail(db.Model, SerializerMixin):
#     __tablename__ = 'order_details'

#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     price = db.Column(db.Float)
#     sku = db.Column(db.Integer)
#     quantity = db.Column(db.Integer)

# class Order(db.Model, SerializerMixin):
#     __tablename__ = 'orders'

#     id = db.Column(db.Integer, primary_key=True)
#     customer_name = db.Column(db.String)
#     email = db.Column(db.String)
#     password = db.Column(db.String)
#     shipping_address = db.Column(db.String)
#     billing_address = db.Column(db.String)
#     order_email = db.Column(db.String)
#     order_date = db.Column(db.DateTime, server_default=db.func.now())
#     order_status = db.Column(db.String)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Add models here
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurants.restaurant_pizzas', '-restaurant_pizzas.pizza')

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    pizza_restaurants = db.relationship('RestaurantPizza', backref = 'pizza')

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-pizzas.pizza_restaurants', '-restaurant_pizzas.restaurant')

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref = 'restaurant')

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-pizza.pizza_restaurants', '-restaurant.restaurant_pizzas')

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    @validates('price')
    def validates_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError("Price must be betweeen 1 and 30, exclusive!")
        return value