"""
 cms
 Created by 带入 on 2020/5/10.
"""

from flask import Blueprint
from app.api.cms import post_handlers

__author__ = '带土'


def create_blueprint_cms():
    blueprint = Blueprint('/api/cms', __name__)
    post_handlers.api.register(blueprint)
    return blueprint
