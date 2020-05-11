'''
shop 处理器
'''

import json, time, datetime, uuid
from app.libs.util import next_id
from app.models.pet_shop_handlers import Shop
from flask import flash, request, jsonify, url_for, redirect
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

__author__ = "带土"

api = Redprint('products')

# 获取商品数据
@api.route("", methods=["GET"])
@auth.login_required
def getProducts():
    _shop = Shop()
    result = _shop.products_findall()
    obj = dict()
    if result:
        obj["resultCode"] = "20000"
        obj["message"] = "ok"
        obj["result"] = result
    else:
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = ""

    return jsonify(obj)
