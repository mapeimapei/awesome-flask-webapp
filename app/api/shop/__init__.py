"""
 shop
 Created by 带土 on 2020/5/10.
"""

from flask import Blueprint
from app.api.shop import products, cart, order

__author__ = '带土'


def create_blueprint_shop():
    blueprint = Blueprint('/api/shop', __name__)
    products.api.register(blueprint)
    cart.api.register(blueprint)
    order.api.register(blueprint)
    return blueprint
