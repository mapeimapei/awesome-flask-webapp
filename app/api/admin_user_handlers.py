'''
后台用户账号处理器
'''
import json, time

from sqlalchemy import or_

from . import api
from ..forms.auth_handlers import LoginForm
from ..libs.util import next_id
from ..models.auth_handlers import User
from flask import render_template, flash, request, jsonify, url_for, redirect

__author__ = "带土"


# @api.route("/login", methods=["POST"])
# def login():
#     args = json.loads(request.data)
#     user = User()
#     result = user.get_user_data(args)
#     data = {}
#     if result:
#         data = {
#             "resultCode": "20000",
#             "message": "ok",
#             "result": result
#         }
#     else:
#         data = {
#             "resultCode": "000000",
#             "message": "faild",
#             "result": {}
#         }
#     return jsonify(data)

@api.route("/login", methods=["POST"])
def login():
    data = {}
    args = json.loads(request.data)
    user = User.query.filter(or_(User.email == args['email'],User.name == args['email'])).first()
    if user and user.check_password(args['passwd']):
        res = user.__dict__
        data = {
            "resultCode": "20000",
            "message": "ok",
            "result": {
                "id": res["_user_id"],
                "name": res["name"],
                "email": res["email"],
                "token": "sdfdsgdg"
            }
        }
    else:
        data = {
            "resultCode": "000000",
            "message": "faild",
            "result": {}
        }
    return jsonify(data)

    #
    #
    #
    # form = LoginForm(json.loads(request.data))
    #
    #
    # if form.validate():
    #     user = User.query.filter_by(email=form.email.data).first()
    #
    #     print("user",user.__dict__ )
    #
    #     res = user.__dict__
    #
    #     if user and user.check_password(form.passwd.data):
    #         data = {
    #             "resultCode": "20000",
    #             "message": "ok",
    #             "result": {
    #                "user_id": res["_user_id"],
    #                "name": res["name"],
    #                "email": res["email"],
    #             }
    #         }
    #     else:
    #         data = {
    #             "resultCode": "000000",
    #             "message": "faild",
    #             "result": {}
    #         }
    #     return jsonify(data)
