'''
后台用户账号处理器
'''
import json, time

from flask_login import login_user
from sqlalchemy import or_
from app.forms.auth_handlers import LoginForm
from app.libs.util import next_id
from app.models.auth_handlers import User
from flask import render_template, flash, request, jsonify, url_for, redirect, current_app

from app.libs.redprint import Redprint

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

__author__ = "带土"

api = Redprint('login')


def generate_auth_token(user_id, name, scope=None):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=current_app.config['TOKEN_EXPIRATION'])
    return s.dumps({
        'user_id': user_id,
        'name': name,
        'scope': scope
    })


@api.route("", methods=["POST"])
def login():
    data = {}
    args = request.json
    print("11111111111")
    user = User.query.filter(or_(User.email == args['account'], User.name == args['account'])).first()
    if user and user.check_password(args['passwd']):
        # Token
        token = generate_auth_token(user['user_id'], user['name'])
        data = {
            "resultCode": "20000",
            "message": "ok",
            "result": {
                "id": user["user_id"],
                "name": user["name"],
                "email": user["email"],
                "token": token.decode('ascii')
            }
        }
    else:
        data = {
            "resultCode": "000000",
            "message": "failed",
            "result": {}
        }
    return jsonify(data)
