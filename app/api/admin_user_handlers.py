'''
后台用户账号处理器
'''
import json, time

from . import api
from ..libs.util import next_id
from ..models.user_handlers import User
from flask import render_template, flash, request, jsonify, url_for, redirect

__author__ = "带土"


@api.route("/login", methods=["POST"])
def login():
    args = json.loads(request.data)
    user = User()
    result = user.get_user_data(args)
    data = {}
    if result:
        data = {
            "resultCode": "20000",
            "message": "ok",
            "result": result
        }
    else:
        data = {
            "resultCode": "000000",
            "message": "faild",
            "result": {}
        }
    return jsonify(data)
