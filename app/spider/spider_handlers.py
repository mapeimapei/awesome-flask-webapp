'''
爬虫处理器
'''
import json, time

from . import spider
from ..models.spider_handlers import Spider
from flask import render_template, flash, request, jsonify, url_for, redirect

__author__ = "带土"

@spider.route("/startSpider", methods=["POST"])
def startSpider():
    spider = Spider()
    count = spider.spiderMain()
    obj = {
        "resultCode": "20000",
        "message": f"网络爬虫收获{count}条数据。",
        "result": count
    }
    return jsonify(obj)
