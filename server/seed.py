#!/usr/bin/env python3

from random import randint, choice as rc

from app import app
from models import db, Product, ProductCategory, Color, Order, OrderDetail

# Remote library imports
# from faker import Faker

if __name__ == '__main__':
    # fake = Faker()
    with app.app_context():
        print('Clearing db...')
        Product.query.delete()
        ProductCategory.query.delete()
        Color.query.delete()
        Order.query.delete()
        OrderDetail.query.delete()

        print('Seeding products...')
        products = [
            Product(name='Item', sku='12345', price='$', images='Pix', weight='Lbs', description='Details', thumbnail='Small-pic', category='Item-type'),
            Product(name='Item', sku='12345', price='$', images='Pix', weight='Lbs', description='Details', thumbnail='Small-pic', category='Item-type'),
            Product(name='Item', sku='12345', price='$', images='Pix', weight='Lbs', description='Details', thumbnail='Small-pic', category='Item-type'),
        ]

        db.session.add_all(products)

        # print('Seeding product_categories...')
        # product_categories = [
        #     ProductCategory(category='Item-type'),
        #     ProductCategory(category='Item-type'),
        #     ProductCategory(category='Item-type'),
        # ]

        # db.session.add_all(product_categories)

        # print('Seeding colors...')
        # colors = [
        #     Color(color='Item-color',),
        #     Color(color='Item-color',),
        #     Color(color='Item-color',),
        # ]

        # db.session.add_all(colors)

        # print('Seeding order_details')
        # order_details = [
        #     OrderDetail(price='$', sku='12345', quantity='1'),
        #     OrderDetail(price='$', sku='12345', quantity='1'),
        #     OrderDetail(price='$', sku='12345', quantity='1'),
        # ]

        # db.session.add_all(order_details)

        print('Seeding orders...')
        orders = [
            Order(customer='Customer-name', email='Email', password='PW', shipping_address='Shipping-address', billing_address='Billing-Address', order_email='Order-email', order_date='Order-date'),
            Order(customer='Customer-name', email='Email', password='PW', shipping_address='Shipping-address', billing_address='Billing-Address', order_email='Order-email', order_date='Order-date'),
            Order(customer='Customer-name', email='Email', password='PW', shipping_address='Shipping-address', billing_address='Billing-Address', order_email='Order-email', order_date='Order-date'),
        ]

        db.session.add_all(orders)

