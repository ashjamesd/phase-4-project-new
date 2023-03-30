#!/usr/bin/env python3

# from random import randint, choice as rc

# from app import app
# from models import db, Product, CategoryProduct, Color, Order, OrderDetail

# Remote library imports
# from faker import Faker

# if __name__ == '__main__':
    # fake = Faker()
    # with app.app_context():
    #     print('Clearing db...')
    #     Product.query.delete()
    #     CategoryProduct.query.delete()
    #     Color.query.delete()
    #     Order.query.delete()
    #     OrderDetail.query.delete()

    #     print('Seeding products...')
    #     products = [
    #         Product(name='Item', sku='12345', price='$', images='Pix', weight='Lbs', description='Details', thumbnail='Small-pic', category='Item-type'),
    #         Product(name='Item', sku='12345', price='$', images='Pix', weight='Lbs', description='Details', thumbnail='Small-pic', category='Item-type'),
    #         Product(name='Item', sku='12345', price='$', images='Pix', weight='Lbs', description='Details', thumbnail='Small-pic', category='Item-type'),
    #     ]

    #     db.session.add_all(products)

        # print('Seeding product_categories...')
        # product_categories = [
        #     CategoryProduct(category='Item-type'),
        #     CategoryProduct(category='Item-type'),
        #     CategoryProduct(category='Item-type'),
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

        # print('Seeding orders...')
        # orders = [
        #     Order(customer='Customer-name', email='Email', password='PW', shipping_address='Shipping-address', billing_address='Billing-Address', order_email='Order-email', order_date='Order-date'),
        #     Order(customer='Customer-name', email='Email', password='PW', shipping_address='Shipping-address', billing_address='Billing-Address', order_email='Order-email', order_date='Order-date'),
        #     Order(customer='Customer-name', email='Email', password='PW', shipping_address='Shipping-address', billing_address='Billing-Address', order_email='Order-email', order_date='Order-date'),
        # ]

        # db.session.add_all(orders)


#!/usr/bin/env python3
from random import choice as rc
# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, Category, Product, CategoryProduct

with app.app_context():

# This will delete any existing rows
# so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Product.query.delete()
    Category.query.delete()
    CategoryProduct.query.delete()

    print("Creating categories...")
    home = Category(name = "Home")
    clothing = Category(name = "Clothing")
    kitchen = Category(name = "Kitchen")
    categories = [home, clothing, kitchen]

    print("Creating products...")
    vase = Product(name = "Zen Vase", price = '30', image="https://a.1stdibscdn.com/early-japanese-satsuma-antique-vase-for-sale/1121189/f_158017521565854320778/15801752_master.jpg?width=768")
    palmShirt = Product(name = "Palm Band Tee", price = '30', image="https://f4.bcbits.com/img/0010232095_10.jpg")
    statue = Product(name = "Buddha Statue", price = '30', image="https://i.etsystatic.com/7293498/r/il/152de0/630306168/il_fullxfull.630306168_7uq7.jpg")
    products = [vase, palmShirt, statue]

    print("Creating CategoryProduct...")

    pr1 = CategoryProduct(category = home, product = vase)
    pr2 = CategoryProduct(category = clothing, product  = palmShirt)
    pr3 = CategoryProduct(category = kitchen, product = statue)
    categoryProducts = [pr1, pr2, pr3]
    db.session.add_all(categories)
    db.session.add_all(products)
    db.session.add_all(categoryProducts)
    db.session.commit()

    print("Seeding done!")