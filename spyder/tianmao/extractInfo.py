# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/12/06
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/11


import os,re

from pyquery import PyQuery as pq
from bs4 import BeautifulSoup as bs


class ExtractInfo():
    '''
    数据提取类，从给定的网页中提取需要的信息
    '''

    def __init__(self):
        # 数据文件路径
        self.datafile_path = os.getcwd() + r"data/commodity/tianmao/item/"
        # 当前工作路径
        self.path = os.getcwd() + r"spyder/tianmao/"


    def get_RankInfo(self,html,file_name):
        """
        解析网页，提取商品排名信息并存储到csv文件
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

            print(info)
            filename = "{}.csv".format(file_name.replace(' ','_'))
            filepath = self.datafile_path + r"original/csv/" + filename

            # 存储商品数据
            with open(filepath,'a',encoding='utf-8') as f:
                f.write(info)

            #sleep(0.5)
            #goodinfo += info
            #return goodinfo

        print("———— <{}>文件写入完成\n".format(file_name))


    def get_GoodRankHtml(self,html):
        """
        提取商品排名页面中每一个商品的网页源码，存储为HTML文件，
        文件名为商品ID。
        param : html (待解析的网页)
        """

        htmlfile_base_path = os.getcwd() + r"/data/commodity/tianmao/item/make/html/"
        doc = pq(html)
        # 遍历该页的所有商品
        for item in doc('#J_ItemList .product').items():
            html = bs(item.html()).prettify()
            # 商品链接
            good_url = item.find('.productImg').attr('href')
            # 正则通配符，匹配‘id=’与‘&skuId’之间的字符
            pattern = re.compile(r'id=(\d)*\b')
            # 商品ID
            commodity_id = pattern.search(good_url).group(0).replace('id=','')
            filename = htmlfile_base_path + "{}.html".format(commodity_id)
            with open(filename,'w',encoding="utf-8") as f:
                f.write(html)
            print("——{}已写入！".format(filename))



    def get_GoodLocation(self,html,file_name):
        """
        解析网页，提取商品位置信息并存储到csv文件
        param : html (待解析的网页)
                file_name (存储的文件名)
        return: locationinfo (提取的信息)
        """



if __name__ == "__main__":

    rank_example_html = os.getcwd() + r"/spyder/tianmao/data/rankExample.html"

    print(rank_example_html)
    with open(rank_example_html,'r', encoding = "utf-8") as f:
        rank_info = f.read()

    with open(rank_example_html, "w", encoding = "utf-8") as f:
        f.write(bs(rank_info).prettify())

    # 实例化
    extractinfo = ExtractInfo()
    extractinfo.get_GoodRankHtml(rank_info)