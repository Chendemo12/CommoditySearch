# -*- encoding: utf-8 -*-
# @Author:  LiChenguang
# @Data  :  2020/02/10
# @Email :  chendemo12@gmail.com
# @sys   :  Ubuntu 18.04
# @WebSite: www.searcher.ltd
# @Last Modified time:  2020/02/10


import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import json,re


class epidemic():
    '''
    获取全国新型冠状病毒发展情况，数据来源：丁香医生、卫健委、微博、央视网
    return:
    '''
    def __init__(self):

        self.dxDoc_url = "https://acs.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?data={%22itemNumId%22%3A%222253282718%22}"


        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

    def dxSpyder(self):
        """获取丁香医生上有关数据"""

        r = requests.get(self.dxDoc_url,headers = self.headers)
        r.encoding = r.status_code

        with open('detail.html','w',encoding = 'utf-8') as f:
            f.write(r.text)

        doc = pq(filename='detail.html')
        print(doc)



if __name__ == "__main__":

   epidemic = epidemic()
   epidemic.dxSpyder()



