# -*- encoding: utf-8 -*-
# @Author:  LiChenguang
# @Data  :  2019/12/05
# @Email :  chendemo12@gmail.com
# @sys   :  Ubuntu 18.04
# @WebSite: www.searcher.ltd
# @Last Modified time:  2020/02/05


import os
import sqlite3


class DatabaseOperate():
    '''
    底层数据库操作类，负责数据库读写
    '''

    def __init__(self):

        # 数据库路径
        self.path = os.getcwd() + r"/data/commodity/database/"
        # 天猫数据库路径
        self.TmDatabase = r"{}tianmao.db".format(self.path)


    def tm_DataInsert(self,sql):
        """
        向天猫数据库插入数据
        param : sql (执行的SQL语句)
        """
        self.conn = sqlite3.connect(self.TmDatabase)
        try:
            self.conn.execute('{}'.format(sql))
            self.conn.commit()
            return True

        except:
            self.conn.rollback()
            return False

        finally:
            self.conn.close()


    def tm_GoodsUrlRead(self):
        return urlList
        pass



if __name__ == "__main__":

    db = DatabaseOperate()
