# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019/11/19
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/12/11

import random,os
from time import sleep

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs

# 数据提取类
from extractInfo import ExtractInfo

class RandomDelay():
    '''
    设置休眠类，引发全局休眠.
    '''

    def __init__(self):
        self.num = random.randint(2,12)

    def delay_1(self):
        num1 = random.randint(1,4)
        sleep(num1*self.num)

    def delay_2(self):
        sleep(self.num)

    def delay_3(self):
        sleep(int(self.num/2))


class TmRankSpyder:
    '''
    爬取天猫指定类别商品排名
        get_Tianmao_Comoditydata()：搜索天猫指定类别商品.
    '''

    def __init__(self):

        self.url = 'https://login.taobao.com/member/login.jhtml'
        self.num = int(1)   # 计数器
        self.path = os.getcwd() + r"/spyder/tianmao/"   # 工作路径

        options = webdriver.ChromeOptions()
        # 不加载图片,加快访问速度
        #options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # 设置为开发者模式
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10) # 超时时长为10s
        # 实例化休眠类
        self.RandomDelay = RandomDelay()
        # 实例化数据提取类
        self.ExtractInfo = ExtractInfo()


    def login(self):
        """登录淘宝"""

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

#######################以下内容暂时无效#######################

    def get_Toalpage(self):
        """
        获取天猫商品总共的页数
        return: page_total(商品总页数)
        """

        # 等待页面加载完毕
        good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_ItemList > div.product > div.product-iWrap')))
        #获取天猫商品总页数
        number_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form')))
        page_total = number_total.text.replace("共","").replace("页，到第页 确定","").replace("，","")

        return page_total


    def next_page(self, page_number):
        """翻页操作"""

        # 等待input输入框加载完毕
        input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form > input.ui-page-skipTo')))

        # 等待确定按钮加载完毕
        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form > button.ui-btn-s')))

        # 清除里面的数字
        input.clear()

        # 重新输入数字
        input.send_keys(page_number)

        # 强制延迟，防止被识别成机器人
        self.RandomDelay.delay_1()

        # 点击确定按钮
        submit.click()


    def swipe_down(self,second):
        """模拟向下滑动浏览"""

        for i in range(int(second/0.1)):
            js = "var q=document.documentElement.scrollTop=" + str(300+200*i)
            self.browser.execute_script(js)
            self.RandomDelay.delay_2()
        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        self.RandomDelay.delay_2()


    def get_Tianmao_ComodityRank(self,search_name):
        """
        爬取天猫商品数据，
        param: search_name(搜索商品名)
        """

        self.browser.get("https://list.tmall.com/search_product.htm?q={}".format(search_name))
        err1 = self.browser.find_element_by_xpath("//*[@id='content']/div/div[2]").text
        err1 = err1[:5]
        if(err1 == "喵~没找到"):
            print("找不到查询的商品")
            return
        try:
            self.browser.find_element_by_xpath("//*[@id='J_ComboRec']/div[1]")
            err2 = self.browser.find_element_by_xpath("//*[@id='J_ComboRec']/div[1]").text
            #print(err2)

            err2 = err2[:5]

            if(err2 == "我们还为您"):
                print("您要查询的商品书目太少了")
                return
        except:
            print("可以爬取这些信息")

        # 获取天猫商品总共的页数
        page_total = self.get_Toalpage()
        print("总共页数" + page_total)

        for page in range(2,int(page_total)):
            """遍历所有页数"""

            # 等待该页面全部商品数据加载完毕
            good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_ItemList > div.product > div.product-iWrap')))

            # 等待该页面input输入框加载完毕
            input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form > input.ui-page-skipTo')))

            # 获取当前页
            now_page = input.get_attribute('value')
            print("当前页数" + now_page + ",总共页数" + page_total)

            # pq模块解析网页源代码
            doc = pq(self.browser.page_source)

            # 遍历该页的所有商品
            for item in  doc('#J_ItemList .product').items():
                info = ""
                good_title = item.find('.productTitle').text().replace('\n',"").replace('\r',"")
                good_status = item.find('.productStatus').text().replace(" ","").replace("笔","").replace('\n',"").replace('\r',"")
                good_price = item.find('.productPrice').text().replace("¥", "").replace(" ", "").replace('\n', "").replace('\r', "")
                good_url = item.find('.productImg').attr('href')
                info = good_title + "," + good_status + "," + good_price + "," + good_url + '\n'
                print(info)
                filename = self.path + "{}.csv".format(search_name)
                # 存储商品数据
                with open(filename,'a',encoding='utf-8') as f:
                    f.write(info)

            # 休眠
            self.RandomDelay.delay_3()
            # 模拟人工向下浏览商品
            self.swipe_down(6)
            # 休眠
            self.RandomDelay.delay_2()

            # 翻页，下一页
            self.next_page(page)

            # 等待滑动验证码出现,超时时间为5秒，每0.5秒检查一次
            # 大部分情况不会出现滑动验证码，所以如果有需要可以注释掉下面的代码
            # sleep(5)
            WebDriverWait(self.browser, 10, 0.5).until(EC.presence_of_element_located((By.ID, "nc_1_n1z"))) #等待滑动拖动控件出现
            try:
                swipe_button = self.browser.find_element_by_id('nc_1_n1z') #获取滑动拖动控件

                #模拟拽托
                action = ActionChains(self.browser) # 实例化一个action对象
                action.click_and_hold(swipe_button).perform() # perform()用来执行ActionChains中存储的行为
                action.reset_actions()
                action.move_by_offset(580, 0).perform() # 移动滑块

            except Exception as e:
                print ('get button failed: ', e)

#######################以上内容暂时无效#######################

    def save_page(self,html,filename):
        """
        存储页面源代码
        param:  html (网页源码)
                filename (网页文件名，为搜索商品名)
        """
        filename = '{}.html'.format(filename.replace(' ','_'))
        filepath = os.getcwd() + r'data/commodity/tianmao/item/original/html/' + filename
        with open(filepath,'w', encoding='utf-8') as f:
            f.write(bs(html).prettify())

    def openTianmao(self,url):
        """
        打开天猫商品页面，用于精简代码
        param : url:商品链接
        return :self.browser.page_source (网页源码)
        """

        # 打开浏览器
        self.browser.get("{}".format(url))
        err1 = self.browser.find_element_by_xpath("//*[@id='content']/div/div[2]").text
        err1 = err1[:5]
        if(err1 == "喵~没找到"):
            print("找不到查询的商品")
            return
        try:
            self.browser.find_element_by_xpath("//*[@id='J_ComboRec']/div[1]")
            err2 = self.browser.find_element_by_xpath("//*[@id='J_ComboRec']/div[1]").text
            #print(err2)

            err2 = err2[:5]

            if(err2 == "我们还为您"):
                print("您要查询的商品书目太少了")
                return
        except:
            print(url)
            print("可以爬取这些信息\n")

        # 等待该页面全部商品数据加载完毕
        good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_ItemList > div.product > div.product-iWrap')))

        # 等待该页面input输入框加载完毕
        input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-page > div.ui-page-wrap > b.ui-page-skip > form > input.ui-page-skipTo')))

        # 返回网页源码
        return self.browser.page_source


    def get_FirstPageRank(self,search_list):
        """
        获取第一页商品排名
        param: search_list(搜索商品名列表)
        """

        # 先查询第一个商品排名页
        search_name = search_list[0]
        url = "https://list.tmall.com/search_product.htm?q={}".format(search_name)
        webpage = self.openTianmao(url)
        # 存储网页源码
        self.save_page(webpage,search_name)
        # 休眠
        self.RandomDelay.delay_2()
        # 提取信息并存储到csv文件
        self.ExtractInfo.get_RankInfo(webpage,search_name)

        for name in search_list[1:]:
            # 搜索下一个商品，新窗口打开连接
            newwindow = 'window.open("https://list.tmall.com/search_product.htm?q={}");'.format(name)
            self.browser.execute_script(newwindow)
            # 移动句柄，对新打开页面进行操作
            self.browser.switch_to_window(self.browser.window_handles[1])

            #######################################################
            ####################### 具体操作 #######################

            page_url = "https://list.tmall.com/search_product.htm?q={}".format(name)
            # 在当前页面下打开链接并获取源码
            web_page = self.openTianmao(page_url)
            # 存储网页源码
            self.save_page(web_page,name)
            # 提取信息并存储到csv文件
            self.ExtractInfo.get_RankInfo(web_page,name.replace(' ','_'))

            # 关闭该新打开的页面
            self.browser.close()
            # 移动句柄到上一个页面
            self.browser.switch_to_window(self.browser.window_handles[0])

            # 休眠
            self.RandomDelay.delay_3()

            #######################################################

        print("———— 程序运行结束！")



if __name__ == "__main__":

    # 搜索商品类别名
    search_list = ['紫米PD快充','半身裙 秋冬','T恤 男大学','羽绒服 女大学生']

    a = TmRankSpyder()
    a.login() #登录
    a.get_FirstPageRank(search_list)

