"""定义基类"""
import time, logging

logging.basicConfig(level=logging.DEBUG)
from sqlalchemy import text
from app.models.base import Base

__author__ = "带土"


class BlogList(Base):
    def __init__(self):
        super().__init__()

    # blog文章列表数据
    def get_single_list(self):
        sql = 'select id,name,summary,content,created_at,user_name from blogs order by created_at desc'
        print(f'sql:{sql}')
        try:
            resultproxy = self.session.execute(
                text(sql)
            )
        except Exception as e:
            print(e)
            res_rows = []
        else:
            res_rows = resultproxy.fetchall()
            self.session.close()

        result = [dict(zip(result.keys(), result)) for result in res_rows]
        for row in result:
            row["created_at"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(row["created_at"]))

        return result

    # 文章详情数据
    def get_single_data(self, id):
        sql = 'select id,name,summary,content,created_at,user_name from blogs where :id = id'
        print(f"sql:{sql}")
        fields = {}

        try:
            resultProxy = self.session.execute(
                text(sql),
                {"id": id}
            )
            res_rows = resultProxy.fetchone()
            fields['id'] = res_rows[0]
            fields['name'] = res_rows[1]
            fields['summary'] = res_rows[2]
            fields['content'] = res_rows[3]
            fields['created_at'] = res_rows[4]
            fields['user_name'] = res_rows[5]
        except Exception as e:
            print(e)
        finally:
            self.session.close()

        print("fields", fields)
        return fields
