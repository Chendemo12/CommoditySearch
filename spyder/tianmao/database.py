# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/12/05
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/05

import os
import sqlite3

class DatabaseOperate():
    '''
    数据库有关类
    '''

    def __init__(self):
        self.path = os.getcwd() + r"/data/commodity/database/"     # 工作路径
        # 数据库路径
        self.database = r"{}commodityItems.db".format(self.path)


    def dataInsert(self,sql):
        """
        把抓取的第一页天猫商品存储到数据库
        param : sql (执行的SQL语句)
        """
        self.conn = sqlite3.connect(self.database)
        try:
            self.conn.execute('{}'.format(sql))
            self.conn.commit()
        except:
            self.conn.rollback()

        finally:
            self.conn.close()


    def createTable_Rank(self,table_name):
        """
        创建商品排名
        param : table_name (创建的表名)
        """

        create_table_sql = """CREATE TABLE '{}' ('id' INTEGER,'商品名称' TEXT,'月成交量' TEXT,'累计评价量' TEXT, '价格' INTEGER, '商品链接' TEXT);""".format(table_name)

        self.conn = sqlite3.connect(self.database)
        try:
            self.conn.execute(create_table_sql)
        except:
            self.conn.rollback()

        finally:
            self.conn.close()


if __name__ == "__main__":

    db = DatabaseOperate()
    summary_file = os.getcwd() + r"data/commodity/tianmao/item/make/csv/Summary.csv"
    with open(summary_file,'r',encoding = 'utf-8') as f:
        goods = f.read()

    goods = goods.split('\n')
    for good in goods:
        print(good)
        sql = '''INSERT INTO commodityList(id,商品名称,月成交量,累计评价量,价格,商品链接) VALUES({})'''.format(good)
        print(sql)
        db.dataInsert(sql)