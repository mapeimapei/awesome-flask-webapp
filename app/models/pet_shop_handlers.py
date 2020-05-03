"""商店模型库"""
import time, datetime, json, decimal, logging
from sqlalchemy import text
from app.models.base import Base2

logging.basicConfig(level=logging.DEBUG)
__author__ = "带土"


class Shop(Base2):
    def __init__(self):
        super().__init__()

    # 删除订单中的商品
    def delete_product_in_order_details(self, args):
        affectedCount = 0
        try:
            sql = 'DELETE FROM orderdetails where orderid = %(orderid)s AND productid = %(productid)s '
            cursor = self.engine.execute(sql, args)
            self.session.commit()
            affectedCount = cursor.rowcount
        except BaseException as e:
            logging.debug(f"删除失败 {e}")
        finally:
            self.session.close()
            return affectedCount

    # 订单详情
    def get_orders_details_by_id(self, args):
        orderObj = {}
        sql = 'select a.orderid, CAST(a.orderdate AS CHAR),a.status,a.amount,b.productid,b.quantity,c.category,' \
              'c.descn,c.image, c.cname,c.listprice from (orderdetails b inner join products c on b.productid = ' \
              'c.productid) inner join orders a on a.orderid = b.orderid where a.userid = :userid and a.orderid = ' \
              ':orderid '

        try:
            resultProxy = self.session.execute(text(sql), args)
            result_set = resultProxy.fetchall()
            orderObj["orderlist"] = []
            orderObj["amount"] = 0
            # 4. 提取结果集
            for row in result_set:
                obj = dict()
                obj['orderid'] = row[0]
                obj['orderdate'] = row[1]
                obj['status'] = row[2]
                obj['amount'] = float(row[3])
                obj['productid'] = row[4]
                obj['quantity'] = row[5]
                obj['category'] = row[6]
                obj['descn'] = row[7]
                obj['image'] = row[8]
                obj['cname'] = row[9]
                obj['listprice'] = row[10]
                orderObj["orderlist"].append(obj)
                orderObj["amount"] += row[10] * row[5]
        except Exception as e:
            logging.debug(f"查询所有订单信息失败 {e}")
        finally:
            self.session.close()
            return orderObj

    # 删除订单
    def delete_order(self, args):
        affectedCount = 0
        try:
            # 删除订单详情数据
            sql = f'DELETE FROM orderdetails where orderid = \'{args["orderid"]}\' '
            self.engine.execute(sql)

            # 删除订单表数据
            sql2 = 'DELETE FROM orders where orderid = %(orderid)s AND userid = %(userid)s '
            self.engine.execute(sql2, args)

            self.session.commit()
            affectedCount = 1
        except BaseException as e:
            logging.debug(f"删除订单失败 {e}")
        finally:
            self.session.close()
            return affectedCount

    # 获取订单列表
    def get_order_list(self, userid):
        orderlist = []
        sql = f'select orderid,cast(orderdate AS char),status ,amount from orders where userid = "{userid}" ORDER BY orderdate desc'
        try:
            resultProxy = self.session.execute(sql)
            result_set = resultProxy.fetchall()
            for row in result_set:
                obj = dict()
                obj['orderid'] = row[0]
                obj['orderdate'] = row[1]
                obj['status'] = row[2]
                obj['amount'] = float(row[3])
                orderlist.append(obj)
        except Exception as e:
            logging.debug(f"查询所有订单信息失败 {e}")
        finally:
            self.session.close()
            return orderlist

    # 生成订单
    def add_order(self, args):
        userid = args["userid"]
        valStr = ""
        productList = json.loads(args["productList"])
        productLists = []
        for item in productList:
            productLists.append(item["productid"])
            valStr += f',(\'{args["orderid"]}\',\'{item["productid"]}\',\'{item["quantity"]}\')'
        affectedCount = 0
        try:

            # 删除购物车的对应数据
            for productid in productLists:
                sql3 = f'delete from cart WHERE userid="{userid}" AND productid="{productid}"'
                self.engine.execute(sql3)

            # 插入订单数据
            sql = 'insert INTO orders (orderid,userid,orderdate,status,amount) VALUES ' \
                  '(%(orderid)s,%(userid)s,%(orderdate)s,%(status)s,%(amount)s)'
            self.engine.execute(sql, args)

            # 插入订单详情数据
            sql2 = 'insert INTO orderdetails (orderid,productid,quantity) ' \
                   'VALUES ' + valStr[1:]
            cursor = self.engine.execute(sql2)

            self.session.commit()
            affectedCount = cursor.rowcount
            logging.info(f"影响的数据行数{affectedCount}")
        except BaseException as e:
            logging.debug(f"生成订单失败 {e}")
        finally:
            self.session.close()
            return affectedCount

    # 根据productids 删除购物车数据
    def delete_cart(self, args):
        affectedCount = 0
        userid = args["userid"]
        try:
            for productid in args["productids"]:
                sql = f'delete from cart WHERE userid="{userid}" AND productid="{productid}"'
                print(f'sql:{sql}')
                cursor = self.engine.execute(sql)

            self.session.commit()
            affectedCount = cursor.rowcount
            logging.info(f"影响的数据行数{affectedCount}")

        except BaseException as e:
            logging.debug(f"删除购物车失败 {e}")
        finally:
            self.session.close()
            return affectedCount

    # 根据userid 获取用户购物车数据
    def get_cart_list(self, userid):
        cartLists = []
        sql = f'SELECT c.productid,c.quantity,p.category, p.image,p.descn,p.listprice,p.cname from cart c,products p ' \
              f'WHERE c.productid = p.productid AND c.userid = "{userid}" '
        try:
            resultProxy = self.session.execute(sql)
            res_rows = resultProxy.fetchall()
            cartLists = [dict(zip(result.keys(), result)) for result in res_rows]
        except Exception as e:
            logging.debug(f"查询所有商品信息失败 {e}")
        finally:
            self.session.close()
            return cartLists

    # add_cart
    def add_cart(self, args):
        affectedCount = 0
        try:
            sql = 'select * from cart WHERE userid = :userid AND productid = :productid'
            resultProxy = self.session.execute(
                text(sql),
                args
            )
            res_row = resultProxy.fetchone()
            sql2 = ""
            if res_row:
                # 如果商品存在，则增加商品数量
                sql2 = 'update cart set quantity = quantity + %(quantity)s WHERE ' \
                       'userid = %(userid)s AND productid = %(productid)s'
            else:
                # 如果商品不存在，则新增
                sql2 = 'insert INTO cart (userid,productid,quantity) VALUES ' \
                       '(%(userid)s,%(productid)s,%(quantity)s)'

            cursor = self.engine.execute(sql2, args)
            self.session.commit()
            affectedCount = cursor.rowcount
            logging.info(f"影响的数据行数{affectedCount}")
        except BaseException as e:
            logging.debug(f"插入文章失败 {e}")

        finally:
            self.session.close()
            return affectedCount

    # 获取所有商品数据
    def products_findall(self):
        """查询所有商品信息"""
        products = []
        sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn from products'
        try:
            resultProxy = self.session.execute(sql)
            res_rows = resultProxy.fetchall()
            for row in res_rows:
                product = dict()
                product['productid'] = row[0]
                product['category'] = row[1]
                product['cname'] = row[2]
                product['ename'] = row[3]
                product['image'] = row[4]
                product['listprice'] = row[5]
                product['unitcost'] = row[6]
                product['descn'] = row[7]
                products.append(product)

        except Exception as e:
            logging.debug(f"查询所有商品信息失败 {e}")
        finally:
            self.session.close()
            return products
