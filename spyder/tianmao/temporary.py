# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/12/11
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/11


import os
from bs4 import BeautifulSoup as bs

def get_GottenGoods():
    """
    获取已经爬取的商品名
    """
    # 获取HTML文件名
    htmlfile_path = os.getcwd() + r"/data/commodity/tianmao/item/original/html/"
    files = os.listdir(htmlfile_path)           # 获取当前目录下的所有html文件
    html_file = []                              # html文件

    for file in files:
        if ".html" in file:
            html_file.append(file)
    return html_file



if __name__ =="__main__":

    files = get_GottenGoods()
    htmlfile_path = os.getcwd() + r"/data/commodity/tianmao/item/original/html/"
    # 格式化HTML代码
    for file in files:
        file_name = htmlfile_path + "{}".format(file)
        with open(file_name,'r',encoding = 'utf-8') as f:
            original_html = f.read()
        with open(file_name, "w", encoding = "utf-8") as f:
            f.write(bs(original_html).prettify())
        print("——{}已修正！".format(file))