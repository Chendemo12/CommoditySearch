# -*- encoding: utf-8 -*-
# @Author:  LiChenguang
# @Data  :  2019/12/05
# @Email :  chendemo12@gmail.com
# @sys   :  Ubuntu 18.04
# @WebSite: www.searcher.ltd
# @Last Modified time:  2020/02/06


import os
import re
import sqlite3
import time

from databaseOperate import DatabaseOperate
from extractInfo import ExtractInfo


class DataClean():
    '''
    将数据清洗后存储到数据库
    '''
    def __init__(self):

        # csv数据文件路径
        self.path = os.getcwd() + r"/data/commodity/tianmao/item/original/csv/"
        self.databaseOperate = DatabaseOperate()
        self.ExtractInfo = ExtractInfo()


    def get_AllGoodsAttributes(self):
        """
        批量提取排名在第一页的商品属性信息，并存储到数据库
        *return sql
        """

        all_GoodsName = self.ExtractInfo.get_GottenGoodsName()
        for goodname in all_GoodsName:
            try:
                self.get_GoodsAttributes(goodname)
            except FileNotFoundError:
                self.ExtractInfo.get_GoodsRankList(goodname)
                self.get_GoodsAttributes(goodname)


    def get_GoodsAttributes(self,filename):
        """
        提取排名在第一页的商品属性信息，并存储到数据库
        param: filename (存储所有商品排名的csv文件)
        *return sql
        """

        # 存储任一类商品排名的csv文件目录
        csv_file_path = r"data/commodity/tianmao/item/original/csv/{}.csv".format(filename)

        # 清空错误记录文件
        with open('log.txt','w',encoding='utf-8') as f:
            f.write("")

        with open(csv_file_path,'r',encoding='utf-8') as fr:
            csv_file_contents = fr.readlines()
        for content in csv_file_contents:
            try:
                # 商品属性
                good_attr = content.split(',')
                url = good_attr[-1].replace('\n','')

                # 正则通配符，匹配‘id=’与‘&skuId’之间的字符
                pattern = re.compile(r'id=(\d)*\b')
                # 商品ID
                commodity_id = pattern.search(url).group(0).replace('id=','')

                #timeStruct = time.time()  # 当前时间戳
                #localtime =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())          # 本地时间

                # 存储到数据库
                sql = '''INSERT INTO commoditylist(id,name,price,创建时间,creation_time,url) VALUES({},"{}","{}","{}","{}","{}")'''.format(commodity_id,good_attr[0],good_attr[-2],str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())),str(time.time()),url)

                if self.databaseOperate.tm_DataInsert(sql):
                    print("———— {} 插入成功！".format(commodity_id))
                else:
                    print("！! {} 插入失败！".format(commodity_id))
                    with open('log.txt','a',encoding='utf-8') as f:
                        f.write(commodity_id)
                        f.write("：天猫商品插入数据库失败，{}".format(str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))))
                        f.write('\n')

            except IndexError:
                pass





if __name__ == "__main__":

    t = DataClean()
    t.get_AllGoodsAttributes()
