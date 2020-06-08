'''
后台CMS处理器
'''
import json, time

from app.libs.redprint import Redprint
from app.libs.util import next_id
from app.models.blog_handlers import BlogList

from flask import render_template, flash, request, jsonify, url_for, redirect

__author__ = "带土"

api = Redprint('post')


# 删除文章数据
@api.route("/deleteSingle", methods=["POST"])
def deleteSingle():
    args = json.loads(request.data)
    blog_list = BlogList()
    result = blog_list.delete_single_data(args)
    data = {}
    if result > 0:
        data = {
            "resultCode": "20000",
            "message": "ok",
            "result": "删除成功"
        }
    else:
        data = {
            "resultCode": "000000",
            "message": "failed",
            "result": "删除失败"
        }
    return jsonify(data)


# 添加文章数据
@api.route("/addSingle", methods=["POST"])
def addSingle():
    args = json.loads(request.data)
    args["post_id"] = args["post_id"] or str(next_id())
    args["user_image"] = "about:blank"
    args["created_at"] = str(time.time())
    blog_list = BlogList()
    result = blog_list.insert_single_data(args)
    data = {}
    if result > 0:
        data = {
            "resultCode": "20000",
            "message": "ok",
            "result": "操作成功"
        }
    else:
        data = {
            "resultCode": "000000",
            "message": "failed",
            "result": "操作失败"
        }
    return jsonify(data)


# 根据ID获取文章详情
@api.route("/getSingleById/<id>", methods=["GET"])
def getSingleById(id):
    blog_list = BlogList()
    result = blog_list.get_single_data(id)
    data = {}
    if result:
        data = {
            "resultCode": "20000",
            "message": "ok",
            "result": result
        }
    else:
        data = {
            "resultCode": "000000",
            "message": "failed",
            "result": {}
        }
    return jsonify(data)


# 获取文章列表数据
@api.route("/getPosts", methods=["GET"])
def getPosts():
    blog_list = BlogList()
    result = blog_list.get_single_list()
    data = {}
    if result:
        data = {
            "resultCode": "20000",
            "message": "ok",
            "result": result
        }
    else:
        data = {
            "resultCode": "000000",
            "message": "failed",
            "result": {}
        }
    return jsonify(data)
