"""爬虫模型库"""
import re, time, logging, uuid, pymysql

from sqlalchemy import text
from app.models.base import Base2
import threading
import urllib.request
from bs4 import BeautifulSoup
from ..libs.util import next_id
from ..models.blog_handlers import BlogList

logging.basicConfig(level=logging.DEBUG)

__author__ = "带土"


class Spider(Base2):
    def __init__(self):
        self.count = 0
        super().__init__()

    def spiderMain(self):
        '''主函数'''
        # 创建列表爬虫线程 listSpiderThread
        listSpiderThread = threading.Thread(target=self.listSpiderThreadBody, name="ListSpiderThread")
        # 启动线程 listSpiderThread
        listSpiderThread.start()
        listSpiderThread.join()
        # 创建列表爬虫线程 contentSpiderThread
        contentSpiderThread = threading.Thread(target=self.contentSpiderThreadBody, name="ContentSpiderThread")
        # 启动线程 contentSpiderThread
        contentSpiderThread.start()
        contentSpiderThread.join()
        return self.count

    def listSpiderThreadBody(self):
        ''' 列表爬虫线程体函数 '''
        t = threading.current_thread()
        print("列表爬虫线程开始", t.name)
        postArr = self.get_ire_posts()
        blog_list = BlogList()
        blogPostArr = blog_list.get_single_list()

        pastsNameArr = []
        for item in blogPostArr:
            pastsNameArr.append(item["name"])
        self.count = self.insert_single_list(postArr, pastsNameArr)
        print("列表爬虫线程结束", t.name, self.count)

    def contentSpiderThreadBody(self):
        ''' 文章爬虫线程体函数 '''
        t = threading.current_thread()
        print("文章爬虫线程开始", t.name)
        spiderContentList = self.get_spider_content_list()
        self.count = 0
        for n in range(len(spiderContentList)):
            url = spiderContentList[n]["url"]
            content = self.get_ire_content(url)
            obj = {
                "content": content,
                "url": url,
            }
            print(obj["url"], obj["content"])
            self.count += self.update_single_data(obj)
            print("第{0}次执行线程{1},更新数据{2}条".format(n, t.name, self.count))
            time.sleep(0.4)
        print("文章爬虫线程结束", t.name)

    # 爬取文章内容
    def get_ire_content(self, url):
        req = urllib.request.Request(url)
        article = ""

        arr = []
        with urllib.request.urlopen(req) as res:
            data = res.read()
            htmlStr = data.decode("gbk")
            soup = BeautifulSoup(htmlStr, 'html.parser')
            arr = soup.select('.m-article p')

        for item in arr:
            article += str(item)

        return re.sub(r'"', '\'', article)

    # 爬取列表
    def get_ire_posts(self):
        url = "http://column.iresearch.cn/"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            data = res.read()
            htmlStr = data.decode("gbk")
            soup = BeautifulSoup(htmlStr, 'html.parser')
            liArr = soup.select('div[data="rootId=2&classId=101"] li')
        postArr = []
        for item in liArr:
            obj = {}
            obj["name"] = str.strip(item.find("h3").find("a").get_text())
            summary = str.strip(item.find("p").get_text())
            obj["summary"] = summary.strip('\n\r ')
            dt = str.strip(item.find("span").get_text())
            timeArray = time.strptime(dt, "%Y/%m/%d %H:%M:%S")
            obj["created_at"] = '%f' % time.mktime(timeArray)
            obj["content"] = str.strip(item.find("h3").find("a").get("href"))
            obj["url"] = str.strip(item.find("h3").find("a").get("href"))

            obj["id"] = str('%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex))
            obj["user_id"] = "00158855657446102ff7cb03a1e4bb08db58fa8acaf7440000"
            obj["user_name"] = "spider"
            obj["user_image"] = "about:blank"

            postArr.append(obj)

        return postArr

    def update_single_data(self, obj):
        """  更新文章数据 """
        # 1 建立数据库连接
        connection = pymysql.connect(host='127.0.0.1',
                                     port=3306,
                                     user='root',
                                     password='mapei123',
                                     db='awesome',
                                     charset='utf8')
        affectedcount = 0
        try:
            # 创建游标对象
            with connection.cursor() as cursor:
                # 3 执行sql操作
                sql = 'update blogs set content = "{0}" WHERE content = "{1}"'.format(obj["content"], obj["url"])
                affectedcount = cursor.execute(sql)
                logging.info(f"影响的数据行数{affectedCount}")
                # 4 提交数据库事务
                connection.commit()
        except pymysql.DatabaseError as error:
            # 5 回滚数据库事务
            connection.rollback()
            logging.debug('插入数据失败' + error)
        finally:
            # 6 关闭数据库连接
            connection.close()
            return affectedcount

    def get_spider_content_list(self):
        """ 查找爬虫文章列表数据 """
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
                sql = 'SELECT id,content FROM blogs WHERE content LIKE "http://%"'
                cursor.execute(sql)
                # 4. 提取结果集
                result_set = cursor.fetchall()
                for row in result_set:
                    fields = {}
                    fields['id'] = row[0]
                    fields['url'] = row[1]
                    data.append(fields)
        except pymysql.DatabaseError as error:
            print('数据查询失败' + error)
        finally:
            # 6 关闭数据库连接
            connection.close()
        return data

    def insert_single_list(self, list, pastsIdArr):
        """  插入文章数据 """
        # 1 建立数据库连接
        connection = pymysql.connect(host='127.0.0.1',
                                     port=3306,
                                     user='root',
                                     password='mapei123',
                                     db='awesome',
                                     charset='utf8')
        affectedcount = 0
        valStr = ""
        for item in list:
            if item["name"] not in pastsIdArr:
                valStr += f',(\'{item["id"]}\',\'{item["user_id"]}\',\'{item["user_name"]}\',\'{item["user_image"]}\',\'{item["name"]}\',\'{item["summary"]}\',\'{item["content"]}\',\'{item["created_at"]}\')'

        try:
            # 创建游标对象
            with connection.cursor() as cursor:
                # 3 执行sql操作
                sql = 'insert into blogs ' \
                      '(id,user_id,user_name,user_image,name,summary,content,created_at)' \
                      ' VALUES ' + valStr[1:]
                print("sql", sql)

                affectedcount = cursor.execute(sql)
                logging.info(f"影响的数据行数{affectedCount}")
                # 4 提交数据库事务
                connection.commit()
        except pymysql.DatabaseError as error:
            # 5 回滚数据库事务
            connection.rollback()
            logging.debug('插入数据失败' + error)
        finally:
            # 6 关闭数据库连接
            connection.close()
            return affectedcount
