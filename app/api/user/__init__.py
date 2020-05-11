"""
 user
 Created by 带土 on 2020/5/10.
"""

from flask import Blueprint
from app.api.user import login

__author__ = '带土'


def create_blueprint_user():
    blueprint = Blueprint('/api/user', __name__)
    login.api.register(blueprint)
    return blueprint
