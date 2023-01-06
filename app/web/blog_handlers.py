'''
blog的视图函数
'''
from flask_login import current_user, login_required

from app.web import web
from app.models.blog_handlers import BlogList
from flask import render_template, flash, request, jsonify, url_for, redirect, session
import time, logging

logging.basicConfig(level=logging.DEBUG)

__author__ = "带土"


@web.route('/404')
def page404():
    return render_template('404.html')


@web.route("/")
#@login_required
def index():
    # name = current_user.name

    blog_list = BlogList()
    result = blog_list.get_single_list()

    return render_template('index.html', blogData=result)


@web.route('/single/<id>')
@login_required
def single(id):
    blog_list = BlogList()
    result = blog_list.get_single_data(id)
    print("11111", current_user)

    if result:
        return render_template('single.html', singleData=result)
    else:
        return redirect(url_for('web.page404'))


@web.route('/admin')
def admin():
    return render_template('admin.html')
