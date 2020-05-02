'''
api 的蓝图
'''

from flask import Blueprint, url_for

__author__ = '带土'

api = Blueprint('api', __name__)
from app.api import admin_user_handlers
from app.api import admin_cms_handlers
