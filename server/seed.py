#!/usr/bin/env python3

# from random import randint, choice as rc

# from app import app
# from models import db, Product, ProductCategory, Color, Order, OrderDetail

# Remote library imports
# from faker import Faker

# if __name__ == '__main__':
    # fake = Faker()
    # with app.app_context():
    #     print('Clearing db...')
    #     Product.query.delete()
    #     ProductCategory.query.delete()
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
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

# This will delete any existing rows
# so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    print("Creating restaurants...")
    shack = Restaurant(name = "Karen's Pizza Shack", address = 'address1')
    bistro = Restaurant(name = "Sanjay's Pizza", address = 'address2')
    palace = Restaurant(name = "Kiki's Pizza", address = 'address3')
    restaurants = [shack, bistro, palace]

    print("Creating pizzas...")


    cheese = Pizza(name = "Emma", ingredients = "Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name = "Geri", ingredients = "Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name = "Melanie", ingredients = "Dough, Sauce, Ricotta, Red peppers, Mustard")
    pizzas = [cheese, pepperoni, california]

    print("Creating RestaurantPizza...")

    pr1 = RestaurantPizza(restaurant = shack, pizza = cheese, price = 1)
    pr2 = RestaurantPizza(restaurant = bistro, pizza  = pepperoni, price = 4)
    pr3 = RestaurantPizza(restaurant = palace, pizza = california, price = 5)
    restaurantPizzas = [pr1, pr2, pr3]
    db.session.add_all(restaurants)
    db.session.add_all(pizzas)
    db.session.add_all(restaurantPizzas)
    db.session.commit()

    print("Seeding done!")