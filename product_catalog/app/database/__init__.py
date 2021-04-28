#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""Database models"""

from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    delete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<Product %r>" % self.name