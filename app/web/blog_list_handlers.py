'''pass'''
from . import web
from ..models.blog_list_handlers import BlogList
from flask import render_template, flash, request, jsonify, url_for, redirect
import time, logging

logging.basicConfig(level=logging.DEBUG)

__author__ = "带土"

@web.route('/404')
def page404():
    return render_template('404.html')

@web.route("/")
def index():
    blog_list = BlogList()
    result = blog_list.get_single_list()
    return render_template('index.html', blogData=result)


@web.route('/single/<id>')
def single(id):
    blog_list = BlogList()
    result = blog_list.get_single_data(id)
    if result:
        return render_template('single.html', singleData=result)
    else:
        return redirect(url_for('.page404'))



