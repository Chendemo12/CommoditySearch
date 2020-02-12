# -*- encoding: utf-8 -*-
# @Author:  LiChenguang
# @Data  :  2019/12/06
# @Email :  chendemo12@gmail.com
# @sys   :  Ubuntu 18.04
# @WebSite: www.searcher.ltd
# @Last Modified time:  2020/02/05


import os
import re

from bs4 import BeautifulSoup as bs
from pyquery import PyQuery as pq


class ExtractInfo():
    '''
    数据提取类，从任一类商品网页中提取信息
    '''

    def __init__(self):
        # 数据文件路径
        self.datafile_path = os.getcwd() + r"/data/commodity/tianmao/item/original/"
        # 当前工作路径
        self.path = os.getcwd() + r"/spyder/tianmao/"


    def get_GottenGoodsName(self):
        """
        获取已经爬取的商品名
        return : html_file (已爬取的商品)
        """
        # 获取HTML文件名
        htmlfile_path = self.datafile_path + 'html/'
        # 获取当前目录下的所有html文件
        files = os.listdir(htmlfile_path)
        html_file = []
        for file in files:
            if ".html" in file:
                file = file.replace('.html', '')
                html_file.append(file)
        return html_file


    def get_AllGoodsRankList(self):
        """
        批量从任一类商品源码中提取商品排名信息
        """
        htmlfiles = self.get_GottenGoodsName()
        for filename in htmlfiles:
            self.get_GoodsRankList(filename)


    def get_AllGoodsHtml(self):
        """
        批量提取每一个商品的网页源码，存储为HTML文件，文件名为商品ID。
        """

        htmlfiles = self.get_GottenGoodsName()
        for filename in htmlfiles:
            self.get_GoodsHtml(filename)


    def get_GoodsRankList(self,filename):
        """
        从任一类商品源码中提取商品排名信息
        param : filename (文件名)
        return: info (提取的商品信息)
        """

        htmlfilepath = self.datafile_path + r"html/{}.html".format(filename)
        csvfilepath = self.datafile_path + r"csv/{}.csv".format(filename)

        with open(htmlfilepath,'r',encoding='utf-8') as f:
            doc = pq(f.read())

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
            info = good_title + "," + good_status + "," + good_price  + "," + "https:{}".format(good_url)

            #info = "'" + good_title + "'," + "'" + good_status + "'," + good_price  + ",'" + "https:{}".format(good_url) + "'\n"

            #print(info)

            # 存储商品数据
            with open(csvfilepath,'a',encoding='utf-8') as f:
                f.write(info)
                f.write('\n')

        print("———— <{}>文件写入完成\n".format(filename))


    def get_GoodsHtml(self,filename):
        """
        提取每一个商品的网页源码，存储为HTML文件，文件名为商品ID。
        param : filename (待解析的网页文件名)
        """

        htmlfilepath = self.datafile_path + r"html/{}.html".format(filename)
        # 把每一个商品信息存储在以下路径内
        goodsfile_base_path = os.getcwd() + r"/data/commodity/tianmao/item/make/html/"

        with open(htmlfilepath,'r',encoding='utf-8') as f:
            doc = pq(f.read())

        # 遍历该页的所有商品
        for item in doc('#J_ItemList .product').items():
            html = bs(item.html()).prettify()
            # 商品链接
            good_url = item.find('.productImg').attr('href')
            # 正则通配符，匹配‘id=’与‘&skuId’之间的字符
            pattern = re.compile(r'id=(\d)*\b')
            # 商品ID
            commodity_id = pattern.search(good_url).group(0).replace('id=','')
            filepath = goodsfile_base_path + "{}.html".format(commodity_id)
            with open(filepath,'w',encoding="utf-8") as f:
                f.write(html)

            print("——{}已写入！".format(commodity_id))


    def get_GoodLocation(self,filename):
        """
        解析网页，提取商品位置信息并存储到csv文件
        param : html (待解析的网页)
                file_name (存储的文件名)
        return: locationinfo (提取的信息)
        """



if __name__ == "__main__":

    # 实例化
    extractinfo = ExtractInfo()
    extractinfo.get_AllGoodsRankList()
