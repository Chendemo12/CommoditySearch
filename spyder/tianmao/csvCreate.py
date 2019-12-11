# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/12/06
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/11


import os

from pyquery import PyQuery as pq

from dataClean import DataClean
from extractInfo import ExtractInfo


class CsvCreate():
    '''
    数据提取类，从给定的网页中提取需要的信息
    '''

    def __init__(self):
        # 数据文件路径
        self.datafile_path = os.getcwd() + r"/data/commodity/tianmao/item/"
        # 当前工作路径
        self.path = os.getcwd() + r"/spyder/tianmao/"
        self.ExtractInfo = ExtractInfo()
        self.DataClean = DataClean()


    def get_GottenGoods(self):
        """
        获取已经爬取的商品名
        """
        # 获取HTML文件名
        htmlfile_path = self.datafile_path + 'original/html/'
        # 获取当前目录下的所有html文件
        files = os.listdir(htmlfile_path)
        html_file = []
        for file in files:
            if ".html" in file:
                file = file.replace('_',' ')
                file = file.replace('.html', '')
                html_file.append(file)
        return html_file


    def get_RankInfo(self,html,file_name):
        """
        解析网页，提取商品排名信息并存储到csv文件，函数和extractInfo.ExtractInfo.get_RankInfo()相同
        param : html (待解析的网页)
                file_name (存储的文件名)
        return: goodinfo (提取商品信息)
        """
        # pq解析网页源码
        doc = pq(html)
        #goodinfo = ""

        # 遍历该页的所有商品
        for item in doc('#J_ItemList .product').items():
            info = ""

            # 商品名称
            good_title = item.find('.productTitle').text().replace('\n',"").replace('\r',"")

            # 商品销量、评价
            good_status = item.find('.productStatus').text().replace(" ","").replace("笔","").replace('\n',"").replace('\r',"")

            #商品价格
            good_price = item.find('.productPrice').text().replace("¥", "").replace(" ", "").replace('\n', "").replace('\r', "")

            # 商品链接
            good_url = item.find('.productImg').attr('href')

            # 组合信息
            info = "'" + good_title + "'," + "'" + good_status + "'," + good_price  + ",'" + "https:{}".format(good_url) + "'\n"

            #print(info)
            filename = "{}.csv".format(file_name.replace(' ','_'))
            filepath = self.datafile_path + r"original/csv/" + filename

            # 存储商品数据
            with open(filepath,'a',encoding='utf-8') as f:
                f.write(info)

        print("———— <{}>文件写入完成\n".format(file_name))


    def csvfile_Create(self):
        """
        从爬取的网页中提取信息，生成 filename.csv 和 filename_make.csv文件
        """
        good_gotten_list = self.get_GottenGoods()
        for i in good_gotten_list:
            try:
                htmlfile = "{}.html".format(i.replace(' ','_'))
                htmlfile_path = r"data/commodity/tianmao/item/original/html/" + htmlfile
                with open(htmlfile_path,'r',encoding = "utf-8") as f:
                    html = f.read()
                csvfile_name = "{}".format(i.replace(' ','_'))
                self.get_RankInfo(html,csvfile_name)

                self.DataClean.rankClean(csvfile_name)
            except FileNotFoundError:
                continue


if __name__ == "__main__":

   t = CsvCreate()
   t.csvfile_Create()
