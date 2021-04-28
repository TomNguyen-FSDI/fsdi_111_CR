#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Smoke tests"""


# To add an ID to our url:
# url = "%s%s" % (BASE_URL, "/products/1")
# the url above is needed for teh following tests:
#test PUT -> requests.put(url, data=whatever_data)
#test DELETE -> requests.delete(url, data=pid)
# test GET (detail page) -> request.get(url)


import requests
BASE_URL = "http://127.0.0.1:5000"


def test_get_all():
    url = "%s%s" % (BASE_URL, "/products")
    out = requests.get(url)
    assert out.text == "Return all products"


def test_create_product():
    url = "%s%s" % (BASE_URL, "/products")
    sample_data = {"product_name": "Banana", "price": 100.00, "quantity": 5}
    out = requests.post(url, data= sample_data)
    assert out.text == "Create new product"
