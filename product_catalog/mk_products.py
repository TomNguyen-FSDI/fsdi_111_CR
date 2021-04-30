#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Sample python code that creates product and displays them."""

from app import db
from app.database import Product, Review

def create_my_product(name, price, quantity):
    """Simple user creation function"""
    db.session.add(
        Product(
            name = name,
            price = price,
            quantity = quantity,
        )
    )
    db.session.commit()


def create_my_review(product_name, user_name, review, star):
    """Simple review creation function"""
    db.session.add(
        Review(
            product_name = product_name,
            user_name = user_name,
            review = review,
            stars = star,
        )
    )
    db.session.commit()

# def update_my_user(id, first_name, last_name, hobbies):
#     """Simple user update function"""
#     db.session.update(
#         User(

#             first_name = first_name,
#             last_name = last_name,
#             hobbies = hobbies
#         )
#     )


#session.delete()
#models.session.new
#jethro.nickname = 'Jetty'
#models.session.dirty
#models.session.commit()

#models.session.query(models.User).order_by(models.Users.column).all()

if __name__ == "__main__":
    create_my_product("Apples", 10.00, 100)
    create_my_product("Oranges", 12.00, 200)
    create_my_product("Peaches", 12.00, 600)
    create_my_review("Apples", "Sherry", "really good", 5)
    create_my_review("Oranges", "Rei", "make some juice", 4)
    create_my_review("Peaches", "Fin", "yummy", 3)
    products = Product.query.all()
    print(products)
