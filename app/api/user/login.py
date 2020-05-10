'''
后台用户账号处理器
'''
import json, time

from flask_login import login_user
from sqlalchemy import or_
from app.forms.auth_handlers import LoginForm
from app.libs.util import next_id
from app.models.auth_handlers import User
from flask import render_template, flash, request, jsonify, url_for, redirect

from app.libs.redprint import Redprint

__author__ = "带土"

api = Redprint('login')


@api.route("", methods=["POST"])
def login():
    data = {}
    args = request.json
    user = User.query.filter(or_(User.email == args['account'], User.name == args['account'])).first()
    if user and user.check_password(args['passwd']):

        login_user(user)
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
