"""blog 模型库"""
import time, logging
from sqlalchemy import text
from app.models.base import Base2

logging.basicConfig(level=logging.DEBUG)
__author__ = "带土"


class BlogList(Base2):
    def __init__(self):
        super().__init__()

    # 删除文章
    def delete_single_data(self, args):
        sql = 'DELETE from blogs WHERE id = %(id)s AND user_id = %(user_id)s'
        affectedCount = 0
        try:
            cursor = self.engine.execute(sql, args)
            self.session.commit()
            affectedCount = cursor.rowcount
            logging.info(f"影响的数据行数{affectedCount}")
        except Exception as e:
            logging.debug(f"删除文章失败 {e}")
        finally:
            self.session.close()
            return affectedCount

    # 插入文章
    def insert_single_data(self, args):
        affectedCount = 0
        try:
            sql = 'select * from blogs WHERE id = :id'
            resultProxy = self.session.execute(text(sql), {"id": args["post_id"]})
            res_row = resultProxy.fetchone()
            sql2 = ""
            if res_row:
                # 更新文章
                sql2 = 'update blogs set ' \
                       'user_name = %(user_name)s,' \
                       'user_id = %(user_id)s,' \
                       'user_image = %(user_image)s,' \
                       'name = %(name)s,' \
                       'summary = %(summary)s,' \
                       'content = %(content)s,' \
                       'created_at = %(created_at)s' \
                       ' WHERE id = %(post_id)s'
            else:
                # 添加文章
                sql2 = 'insert into blogs ' \
                       '(id,user_id,user_name,user_image,name,summary,content,created_at)' \
                       'VALUES (%(post_id)s,%(user_id)s,%(user_name)s,%(user_image)s,%(name)s,%(summary)s,%(content)s,' \
                       '%(created_at)s) '

            cursor = self.engine.execute(sql2, args)
            self.session.commit()
            affectedCount = cursor.rowcount
            logging.info(f"影响的数据行数{affectedCount}")
        except BaseException as e:
            logging.debug(f"插入文章失败 {e}")

        finally:
            self.session.close()
            return affectedCount

    # 根据ID获取文章详情
    def get_single_data(self, id):
        sql = 'select id,name,summary,content,created_at,user_name from blogs where id = :id'
        fields = {}
        try:
            resultProxy = self.session.execute(text(sql), {"id": id})
            res_row = resultProxy.fetchone()
            if res_row:
                fields['id'] = res_row[0]
                fields['name'] = res_row[1]
                fields['summary'] = res_row[2]
                fields['content'] = res_row[3]
                fields['created_at'] = res_row[4]
                fields['user_name'] = res_row[5]
        except Exception as e:
            logging.debug("获取文章详情 {0}".format(e))
        finally:
            self.session.close()
        return fields

    # blog文章列表数据
    def get_single_list(self):
        sql = 'select id,name,summary,content,created_at,user_name from blogs order by created_at desc'
        try:
            resultProxy = self.session.execute(sql)
        except Exception as e:
            print(e)
            res_rows = []
        else:
            res_rows = resultProxy.fetchall()
            self.session.close()

        result = [dict(zip(result.keys(), result)) for result in res_rows]
        for row in result:
            row["created_at"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(row["created_at"]))

        return result
