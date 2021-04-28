#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Route definitions"""

from flask import render_template, request, redirect, url_for, flash
from app import app, db
from datetime import datetime
from app.database import Product
from app.forms.products import ProductForm

@app.route("/version")
def version():
    version = {
        "ok" : True,
        "message" : "success",
        "version" : "1.0.0",
        "server time" : datetime.now().strftime("%F %H:$M:$S"),
    }
    return render_template("version.html", version=version)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/products")
def get_products():
    """Retrieve all products"""
    products = Product.query.filter_by(delete=False).all()
    return render_template("products.html", product_list = products)


@app.route('/products/all')
def products_all():
    product = Product.query.all()
    return render_template("users_all.html", products = product)


@app.route("/products/create", methods=["POST"])
def create_product():
    """Create a new product"""
    form = ProductForm(request.form)
    if form.validate():
        product = Product()
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.description = form.description.data
        db.session.add(product)
        db.session.commit()
        flash("Product created!")
        return redirect(url_for('get_products'))
    flash("Invalid data")
    return redirect(url_for('get_products'))


@app.route("/products/register")
def register():
    return render_template("register.html", form=ProductForm())


@app.route("/products/<int:pid>")
def get_product_detail(pid):
    """Retrieve a single product"""
    product = Product.query.filter_by(id=pid).first()
    return render_template("product_detail.html", product=product)


@app.route("/products/update/<int:pid>", methods=['POST', "PUT"])
def update_product(pid):
    """Update a single product"""
    form = ProductForm(request.form)
    if form.validate():
        product = Product.query.filter_by(id=pid).first()
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.description = form.description.data
        db.session.commit()
        flash("{} Product updated!".format(product.name))
        return redirect(url_for('get_products'))
    flash("Invalid data")
    return redirect(url_for('get_products'))


@app.route("/products/update/form/<int:pid>")
def update_product_form(pid):
    """Renders a form to update"""
    form = ProductForm()
    product = Product.query.filter_by(id=pid).first()
    return render_template("update_form.html", form=form, product=product)



@app.route("/products/delete/<int:pid>")
def delete_product(pid):
    """soft Delete a single product"""
    product = Product.query.filter_by(id=pid).first()
    product.delete = True
    db.session.commit()
    flash("{} soft deleted".format(product.name))
    return redirect(url_for('get_products'))


@app.route("/products/delete/undo/<int:pid>")
def delete_undo(pid):
    """undo soft Delete a single product"""
    product = Product.query.filter_by(id=pid).first()
    product.delete = False
    db.session.commit()
    return redirect(url_for('products_all'))


@app.errorhandler(404)
def page_not_found(e):
    """When a page is not found take to the 404.html"""
    return render_template('404.html'), 404