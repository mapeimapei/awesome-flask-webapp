'''
shop 的蓝图
'''

from flask import Blueprint, url_for

__author__ = '带土'

shop = Blueprint('shop', __name__)

from app.pet_shop import pet_shop_handlers
