'''
shop 处理器
'''

import json, time, datetime, uuid
from app.libs.util import next_id
from app.models.pet_shop_handlers import Shop
from flask import flash, request, jsonify, url_for, redirect
from app.libs.redprint import Redprint

__author__ = "带土"

api = Redprint('order')


# 删除订单中的商品
@api.route("/deleteProductInOrderDetails", methods=["POST"])
def deleteProductInOrderDetails():
    args = json.loads(request.data)
    _shop = Shop()
    obj = dict()
    try:
        result = _shop.delete_product_in_order_details(args)
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


# 订单详情
@api.route("/getOrdersDetailsById", methods=["POST"])
def getOrdersDetailsById():
    args = json.loads(request.data)
    _shop = Shop()
    obj = dict()
    try:
        result = _shop.get_orders_details_by_id(args)
        if result:
            obj["resultCode"] = "20000"
            obj["message"] = "ok"
            obj["result"] = result
        else:
            obj["resultCode"] = "00001"
            obj["message"] = "faild"
            obj["result"] = ""
    except BaseException as e:
        print("error", type(e))
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = "%s" % e

    return jsonify(obj)


# 删除订单
@api.route("/deleteOrder", methods=["POST"])
def deleteOrder():
    args = json.loads(request.data)
    _shop = Shop()
    obj = dict()
    try:
        result = _shop.delete_order(args)
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


# 获取订单数据
@api.route("/getOrderList/<userid>", methods=["GET"])
def getOrderList(userid):
    _shop = Shop()
    result = _shop.get_order_list(userid)
    print(result)
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


# 生成订单
@api.route("/addOrder", methods=["POST"])
def addOrder():
    args = json.loads(request.data)
    args["amount"] = 0
    for item in args["productList"]:
        args["amount"] += item["listprice"] * item["quantity"]

    args["orderid"] = str(uuid.uuid4().hex)
    args["orderdate"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    args["status"] = 0
    args["productList"] = json.dumps(args["productList"])

    _shop = Shop()
    obj = dict()
    try:
        result = _shop.add_order(args)
        if result > 0:
            obj["resultCode"] = "20000"
            obj["message"] = "ok"
            obj["result"] = {"orderid": args["orderid"]}
        else:
            obj["resultCode"] = "00001"
            obj["message"] = "faild"
            obj["result"] = "生成订单失败"
    except BaseException as e:
        print("error", type(e))
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = "%s" % e

    return jsonify(obj)
