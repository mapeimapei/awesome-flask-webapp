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

api = Redprint('cart')


# 删除购物车数据
@api.route("/deleteCart", methods=["POST"])
@auth.login_required
def deleteCart():
    args = json.loads(request.data)
    _shop = Shop()
    obj = dict()
    try:
        result = _shop.delete_cart(args)
        if result > 0:
            obj["resultCode"] = "20000"
            obj["message"] = "ok"
            obj["result"] = ""
        else:
            obj["resultCode"] = "00001"
            obj["message"] = "faild"
            obj["result"] = "删除失败"

    except BaseException as e:
        print("error", type(e))
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = "%s" % e

    return jsonify(obj)


# 获取购物车数据
@api.route("/getCartList/<userid>", methods=["GET"])
@auth.login_required
def getCartList(userid):
    _shop = Shop()
    result = _shop.get_cart_list(userid)
    obj = dict()
    try:
        if result:
            obj["resultCode"] = "20000"
            obj["message"] = "ok"
            obj["result"] = result
        else:
            obj["resultCode"] = "20000"
            obj["message"] = "faild"
            obj["result"] = []
    except BaseException as e:
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = e

    return jsonify(obj)


# 购物车添加
@api.route("/addCart", methods=["POST"])
@auth.login_required
def addCart():
    args = json.loads(request.data)
    _shop = Shop()
    obj = dict()
    try:
        result = _shop.add_cart(args)
        if result == 1:
            obj["resultCode"] = "20000"
            obj["message"] = "ok"
            obj["result"] = ""
        else:
            obj["resultCode"] = "00001"
            obj["message"] = "faild"
            obj["result"] = "添加失败"
    except BaseException as e:
        print("error", type(e))
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = "%s" % e

    return jsonify(obj)
