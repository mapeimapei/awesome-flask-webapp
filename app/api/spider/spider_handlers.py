'''
爬虫处理器
'''
import json, time

from app.models.spider_handlers import Spider
from flask import render_template, flash, request, jsonify, url_for, redirect
from app.libs.redprint import Redprint

__author__ = "带土"

api = Redprint('startSpider')


@api.route("", methods=["POST"])
def startSpider():
    _spider = Spider()
    count = _spider.spiderMain()
    obj = {
        "resultCode": "20000",
        "message": f"网络爬虫收获{count}条数据。",
        "result": count
    }
    return jsonify(obj)
