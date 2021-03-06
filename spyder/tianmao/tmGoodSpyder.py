# -*- encoding: utf-8 -*-
# @Author:  LiChenguang
# @Data  :  2019/12/06
# @Email :  chendemo12@gmail.com
# @sys   :  Ubuntu 18.04
# @WebSite: www.searcher.ltd
# @Last Modified time:  2020/02/06


import os
import random
from time import sleep

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 随机延迟类，天猫商品爬虫
from tmRankSpyder import RandomDelay, TmRankSpyder


class TmGoodSpyder():
    '''
    爬取指定天猫商品信息
    '''

    def __init__(self):

        # 数据文件路径
        self.path = os.getcwd() + r"/TaoBao/data/"

        options = webdriver.ChromeOptions()
        # 不加载图片,加快访问速度
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # 设置为开发者模式
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10) # 超时时长为10s
        # 实例化休眠类，天猫商品爬虫类，数据提取类
        self.RandomDelay = RandomDelay()
        self.TmRankSpyder = TmRankSpyder()
        self.ExtractInfo = ExtractInfo()


    def login(self):
        """
        登录淘宝，非必须
        """

        self.browser.get(self.url)
        # 等待网页加载完成
        self.browser.implicitly_wait(30)

        print("请在20秒内手动登录淘宝！")
        sleep(15)

        # 确定是否登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))

        # 输出淘宝昵称
        print(taobao_name.text + '{}'.format('—————已成功登录！'))


    def get_GoodsUrl(self):
        return urlList
        pass


    def savePage(self,html,filename):
        """
        存储页面源代码
        param:  html (网页源码)
                filename (网页文件名，为商品ID)
        """
        filename = '{}.html'.format(filename)
        filepath = self.path + filename
        with open(filepath,'w', encoding='utf-8') as f:
            f.write(html)


    def openTianmao(self,url):
        """
        打开天猫商品页面，用于精简代码，代码引用于 “tmRankSpyder.TmRankSpyder.openTianmao()”
        param : url:商品链接
        return :self.browser.page_source (网页源码)
        """
        return self.TmRankSpyder.openTianmao(url)







if __name__ == "__main__":

    # 搜索商品类别名
    search_list = ['紫米PD快充','半身裙 秋冬','T恤 男大学','保温杯','羽绒服 女大学生']

    a = TmGoodSpyder()
    a.login() #登录
    a.get_FirstPageRank(search_list)
