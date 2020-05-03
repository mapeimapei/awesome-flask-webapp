'''
user handlers
'''
from . import web
from ..libs.util import next_id
from ..models.auth_handlers import User
from flask import render_template, flash, request, jsonify, url_for, redirect
import time, logging

logging.basicConfig(level=logging.DEBUG)

__author__ = "带土"


# 这里需要优化
@web.route("/register2")
def register2():
    return render_template('register.html')
