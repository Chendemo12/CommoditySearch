# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/12/05
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/11

import os,re
import sqlite3

from database import DatabaseOperate


class DataClean():
    '''
    数据清洗类
    '''
    def __init__(self):
        self.path = os.getcwd() + r"/data/commodity/tianmao/item/make/"  # 数据文件路径
        self.databaseOperate = DatabaseOperate()    # 数据库操作类
        self.goodlist_file = os.getcwd() + r'/spyder/tianmao/goodList.csv'  # 淘宝搜索商品名


    def rankClean(self,file_name):
        """
        对爬取的第一页商品排名csv文件进行格式化，
        从商品链接中提取商品ID，并调用 database.dataInsert() 函数存储到数据库
        param :file_name (待整理的csv文件),并将文件名中的空格替换为"_"
        """
        # 爬取的商品csv文件目录
        csv_file_path = r"data/commodity/tianmao/item/original/csv/{}.csv".format(file_name.replace(' ','_'))

        new_filename = "{}_make.csv".format(file_name.replace(' ','_'))
        new_filepath = self.path + r"csv/" + new_filename

        # 写入新文件首行标题
        with open(new_filepath,'w',encoding='utf-8') as fa:
            fa.write("id,名称,月成交量,累计评价量,价格,商品链接\n")

        with open(csv_file_path,'r',encoding='utf-8') as fr:
            csv_file_contents = fr.readlines()
        for content in csv_file_contents:
            content = content.replace('月成交','')
            content = content.replace("评价","','")
            content = content.replace('旺旺在线','')

            # 正则通配符，匹配‘id=’与‘&skuId’之间的字符
            pattern = re.compile(r'id=(\d)*\b')
            # 商品ID
            commodity_id = pattern.search(content).group(0).replace('id=','')
            print("————{}:已提取————\n".format(commodity_id))

            row = commodity_id + "," + content

            # 写入新文件
            with open(new_filepath,'a',encoding='utf-8') as fa:
                fa.write(row)

            """
            # 存储到数据库
            sql = '''INSERT INTO {}(id,商品名称,月成交量,累计评价量,价格,商品链接) VALUES({})'''.format(file_name.replace(' ','_'),row.replace('\n',''))
            self.databaseOperate.dataInsert(sql)
            """

        print(("————{}已写入\n\n".format(new_filename)))


    def rankSummery(self,file_name):
        """
        对爬取的第一页商品排名csv文件进行格式化，
        从商品链接中提取商品ID，并调用 database.dataInsert() 函数存储到数据库
        param :file_name (待整理的csv文件),并将文件名中的空格替换为"_"
        """

        # 需要汇总的文件路径
        csv_file_path = r"data/commodity/tianmao/item/original/csv/{}.csv".format(file_name.replace(' ','_'))

        summary_filename = "Summary.csv"
        summary_filepath = r"data/commodity/tianmao/item/make/csv/" + summary_filename

        # 写入新文件首行标题
        with open(csv_file_path,'r',encoding='utf-8') as fr:
            csv_file_contents = fr.readlines()
        for content in csv_file_contents:
            content = content.replace('月成交','')
            content = content.replace("评价","','")
            content = content.replace('旺旺在线','')

            # 正则通配符，匹配‘id=’与‘&skuId’之间的字符
            pattern = re.compile(r'id=(\d)*\b')
            # 商品ID
            commodity_id = pattern.search(content).group(0).replace('id=','')
            print("————{}:已提取————\n".format(commodity_id))

            row = commodity_id + "," + content

            # 写入新文件
            with open(summary_filepath,'a',encoding='utf-8') as fa:
                fa.write(row)


        print("————已写入\n\n")


    def get_GoodsList(self):
        """
        从文件读取搜索商品名
        return: good_list (商品名列表)
        """
        with open(self.goodlist_file,'r',encoding = 'utf-8') as f:
            goods = f.read()
        good_list = goods.split('\n')

        return good_list




if __name__ == "__main__":

    good_gotten_file = os.getcwd() + r'/spyder/tianmao/good_gotten.csv'  # 淘宝已爬取商品名
    with open(good_gotten_file,'r',encoding = 'utf-8') as f:
        good_gotten = f.read()
    good_gotten_list = good_gotten.split('\n')

    """
    table_list = ['紫米PD快充']
    s_list = ['保温杯']
    # 实例化数据库操作类
    t = DatabaseOperate()
    for table in table_list:
        # 创建数据库
        t.createTable_Rank(table.replace(' ','_'))
    """

    dataclean = DataClean()
    for filename in good_gotten_list:
        try:
            dataclean.rankSummery(filename)
        except FileNotFoundError:
            continue
