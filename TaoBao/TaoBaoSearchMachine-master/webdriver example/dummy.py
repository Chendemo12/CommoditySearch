# -*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep    
from selenium.common.exceptions import NoSuchElementException
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
item = "Stm32f103c8t6"
# print item
print item
# create a new Chrome session
driver = webdriver.Chrome()
#driver.implicitly_wait(30)
#driver.maximize_window()
#driver1 = webdriver.Chrome()


# navigate to the application home page
#driver.get("https://world.taobao.com")
driver.get("https://world.taobao.com")

search = driver.find_element_by_class_name("yenaeng")
'''
s = "https://xintaiwei.taobao.com/search.htm?search=y&keyword=stm32f103c8t6&lowPrice=&highPrice="
x = s.find(".taobao")
s = s[:x] + ".world" + s[x:]
print s
driver1.get(s)
driver.implicitly_wait(10)
search = driver.find_element_by_xpath("//input[@name='q']")

search = driver.find_element_by_xpath("//input[@name='q']/following-sibling::input")
search1 = driver.find_element_by_xpath("//input[@title='提交']")
search2 = driver1.find_element_by_xpath("//li[@data-searchtype='thisshop']")
search2.click()
print search
print search1
'''
'''
# get the search textbox
search_field = driver.find_element_by_name("q")
 
# enter search keyword and submit
search_field.send_keys(item)
search_field.submit()

# reached Stm32f103c8t6 searching page
# get the area that linked to the seller page
shop = driver.find_elements_by_xpath("//div[@class='shop']")
shop_name = []

shop_html = shop[0].get_attribute('innerHTML')
s = BeautifulSoup(shop_html,'html.parser')
for shop_span in s.find_all('span'):
    if(shop_span.get('class')== None):
        shop_name.append(shop_span.string)
#shop[28].click()
#driver.switch_to_window(driver.window_handles[1])

total = driver.find_element_by_xpath("//div[@class='total']")
x=int(re.search(r'\d+',total.text).group())
for pages in range(x):
    next_page = driver.find_element_by_xpath("//li[@class='item next']")
    next_page.click()
    driver.implicitly_wait(100)
'''
