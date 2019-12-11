# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/12/11
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/11


import os

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
            file = file.replace('_',' ')
            file = file.replace('.html', '')
            html_file.append(file)
    return html_file



if __name__ =="__main__":
    file = get_GottenGoods()
    print(file)