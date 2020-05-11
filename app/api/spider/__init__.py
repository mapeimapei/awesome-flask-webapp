"""
 spider
 Created by 带土 on 2020/5/10.
"""

from flask import Blueprint
from app.api.spider import spider_handlers

__author__ = '带土'


def create_blueprint_spider():
    blueprint = Blueprint('/api/spider', __name__)
    spider_handlers.api.register(blueprint)
    return blueprint
