import time

from flask import jsonify

from flask import render_template, flash, request
import pymysql
import logging;

logging.basicConfig(level=logging.DEBUG)

from . import web

from flask_sqlalchemy import SQLAlchemy

__author__ = "带土"


def get_blog_data():
    """ 获取列表数据 """
    # 1 建立数据库连接
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='mapei123',
                                 db='awesome',
                                 charset='utf8')
    # 要返回的数据
    data = []
    try:
        # 创建游标对象
        with connection.cursor() as cursor:
            # 3 执行sql操作
            sql = 'select id,name,summary,created_at,user_name from blogs order by created_at desc'
            cursor.execute(sql)
            # 4. 提取结果集
            result_set = cursor.fetchall()
            for row in result_set:
                fields = {}
                fields['id'] = row[0]
                fields['name'] = row[1]
                fields['summary'] = row[2]
                fields['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(row[3]))
                fields['user_name'] = row[4]
                data.append(fields)
    except pymysql.DatabaseError as error:
        print('数据查询失败' + error)
    finally:
        # 6 关闭数据库连接
        connection.close()
    return data


@web.route('/demoApi1')
def demoApi1():
    obj = {}
    try:
        obj["resultCode"] = "20000"
        obj["message"] = "ok"
        obj["result"] = get_blog_data()
    except BaseException as e:
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = null

    return obj


@web.route('/hello')
def hello():
    return "hello 安媛媛1."


@web.route('/test2')
def test2():
    r = {
        'name': 'mapei',
        'age': 35
    }

    # 模板
    return render_template('test.html', data=r)


@web.route('/test/<q>/<page>')
def test(q, page):
    print(q, page)
    obj = {"q": q, "page": page}

    # return json.dumps(obj)
    return jsonify(obj)
