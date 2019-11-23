# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/11/19
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/11/22


import random
from time import sleep

from loguru import logger
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# 配置日志记录
logger.debug('this is a debug message')
logger.add('runtime.log')

class TaobaoSpyder:

    def __init__(self):

        self.url = 'https://login.taobao.com/member/login.jhtml'

        options = webdriver.ChromeOptions()
        # 设置为开发者模式，防止被各大网站识别为Selenium
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    def scan_Login(self):
        """扫码登录淘宝."""

        print("—— 请在30秒内扫码完成登陆！")
        self.browser.get(self.url)

        # 选择扫码登录
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_class_name('login-switch').click()

        sleep(20)

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))

        print("{}已登录".format(taobao_name))


    def swipe_down(self, second):
        """模拟向下滑动浏览"""

        for i in range(int(second/0.1)):
            # 根据i的值，模拟上下滑动
            if(i%2==0):
                js = "var q=document.documentElement.scrollTop=" + str(300+400*i)
            else:
                js = "var q=document.documentElement.scrollTop=" + str(200 * i)
            self.browser.execute_script(js)
            sleep(2)

        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        sleep(3)


    # 爬取淘宝 我已买到的宝贝商品数据
    def crawl_good_buy_data(self):

        # 对我已买到的宝贝商品数据进行爬虫
        self.browser.get("https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm")

        # 遍历所有页数
        for page in range(1,100):

            # 等待该页面全部已买到的宝贝商品数据加载完毕
            good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tp-bought-root > div.js-order-container')))

            # 获取本页面源代码
            html = self.browser.page_source

            # pq模块解析网页源代码
            doc = pq(html)

            # # 存储该页已经买到的宝贝数据
            good_items = doc('#tp-bought-root .js-order-container').items()

            # 遍历该页的所有宝贝
            for item in good_items:
                good_time_and_id = item.find('.bought-wrapper-mod__head-info-cell___29cDO').text().replace('\n',"").replace('\r',"")
                good_merchant = item.find('.seller-mod__container___1w0Cx').text().replace('\n',"").replace('\r',"")
                good_name = item.find('.sol-mod__no-br___1PwLO').text().replace('\n', "").replace('\r', "")
                # 只列出商品购买时间、订单号、商家名称、商品名称
                # 其余的请自己实践获取
                print(good_time_and_id, good_merchant, good_name)

            print('\n\n')

            # 大部分人被检测为机器人就是因为进一步模拟人工操作
            # 模拟人工向下浏览商品，即进行模拟下滑操作，防止被识别出是机器人
            # 随机滑动延时时间
            swipe_time = random.randint(1, 3)
            self.swipe_down(swipe_time)


            # 等待下一页按钮 出现
            good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-next')))
            # 点击下一页按钮
            good_total.click()
            sleep(2)


if __name__ == "__main__":

    a = TaobaoSpyder()
    a.scan_Login()
    a.crawl_good_buy_data()
