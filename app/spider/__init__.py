from flask import Blueprint, url_for

__author__ = '七月'

spider = Blueprint('spider', __name__)

from app.spider import spider_handlers

