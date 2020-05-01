import time

from flask import render_template, flash, request, jsonify
import pymysql
import logging

from ..secure import SQLALCHEMY_DATABASE_URI

logging.basicConfig(level=logging.DEBUG)

from . import web

# from flask_sqlalchemy import SQLAlchemy


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text, Integer, Float

__author__ = "带土"


def get_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=10, pool_recycle=7200,
                           pool_pre_ping=True, encoding='utf-8')

    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    return session

def get_blog_data2():
    session = get_session()

    sql = 'select id,name,summary,content,created_at,user_name from blogs order by created_at desc'

    print(f'sql:{sql}')
    try:
        resultproxy = session.execute(
            text(sql)
        )
    except Exception as e:
        print(e)
        res_rows = []
    else:
        res_rows = resultproxy.fetchall()
        session.close()

    result = [dict(zip(result.keys(), result)) for result in res_rows]

    for row in result:
        row["created_at"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(row["created_at"]))

    print(result)
    return result

@web.route("/demoindex")
def demoindex():
    result = get_blog_data2()
    return render_template('index.html', blogData=result)


def get_cart_list(user_id):
    session = get_session()
    sql = """
        SELECT c.productid,c.quantity,p.category, p.image,p.descn,p.listprice,p.cname from cart c,products p WHERE c.productid = p.productid AND c.userid  = :user_id
        """

    print(f'sql:{sql}')
    try:
        resultproxy = session.execute(
            text(sql),
            {"user_id": user_id}
        )
    except Exception as e:
        print(e)
        res_rows = []
    else:
        res_rows = resultproxy.fetchall()
        session.close()

    result = [dict(zip(result.keys(), result)) for result in res_rows]
    print(result)
    return result

@web.route("/api/demoGetCartList", methods=['POST'])
def demoGetCartList():
    user_id = request.form["user_id"]
    obj = {}
    try:
        obj["resultCode"] = "20000"
        obj["message"] = "ok"
        obj["result"] = get_cart_list(user_id)
    except BaseException as e:
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = null

    return obj


@web.route("/api/demoPost", methods=['POST'])
def demoPost():
    name = request.form["name"]
    id = request.form['id']

    print(name, id)
    obj = {
        "name":name,
        "id":id
    }
    return obj


def get_user_data():
    session = get_session()
    sql = "select name,email from users"
    print(f'sql:{sql}')
    try:
        resultproxy = session.execute(text(sql))
    except Exception as e:
        print(e)
        res_rows = []
    else:
        res_rows = resultproxy.fetchall()
        session.close()

    result = [dict(zip(result.keys(), result)) for result in res_rows]
    print(result)
    return result


@web.route('/demoUsers')
def demoUsers() -> object:
    obj = {}
    try:
        obj["resultCode"] = "20000"
        obj["message"] = "ok"
        obj["result"] = get_user_data()
    except BaseException as e:
        obj["resultCode"] = "00000"
        obj["message"] = "faild"
        obj["result"] = null

    return obj


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
