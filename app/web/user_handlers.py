'''pass'''
from . import web
from ..libs.util import next_id
from ..models.user_handlers import User
from flask import render_template,flash, request, jsonify,url_for,redirect
import time, logging
logging.basicConfig(level=logging.DEBUG)


__author__ = "带土"

@web.route("/register")
def register():
    return render_template('register.html')

@web.route("/api/register",methods=["POST"])
def api_register():
    obj = {}
    obj["name"] = request.form['name'].strip()
    obj["email"] = request.form['email']
    obj["passwd"] = request.form['passwd']
    obj["address"] = request.form['address']
    obj["tel"] = request.form['tel']
    obj["id"] = str(next_id())
    obj["admin"] = 0
    obj["image"] = "about:blank"
    obj["created_at"] = str(time.time())

    user = User()
    result = user.insert_register_data(obj)
    if result > 0:
        return redirect(url_for(".index"))
    else:
        return redirect(url_for('.page404'))

