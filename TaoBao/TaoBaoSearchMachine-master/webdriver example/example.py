import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from selenium import webdriver
from urlparse import urljoin
import time
from selenium.webdriver.common.keys import Keys

class CompItem(scrapy.Item):
    model_name = scrapy.Field()
    model_link = scrapy.Field()
    url  =scrapy.Field()

class criticspider(CrawlSpider):
    name = "paytm_l"
    allowed_domains = ["paytm.com"]
    start_urls = ["https://paytm.com/shop/g/electronics/mobile-accessories/mobiles"]


    def __init__(self, *args, **kwargs):
        super(criticspider, self).__init__(*args, **kwargs)
        self.download_delay = 0.25
        self.browser = webdriver.Chrome()

        self.browser.implicitly_wait(2)

    def parse_start_url(self, response):
        self.browser.get(response.url)
        #sites = response.xpath('//div[@class="single-review"]/div[@class="review-header"]')
        self.browser.implicitly_wait(30)

        items = []
        time.sleep(20)
    #   for i in range(0,200):
            #self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        sel = Selector(text=self.browser.page_source)
        sites = sel.xpath('//div[contains(@class,"overflow-hidden")]')

        item = CompItem()

        for r in range(1,5):


                    #item['model_name'] = site.xpath('.//p[contains(@ng-if,"applyLimit")]/text()')
                    button = self.browser.find_element_by_xpath("/html/body/div[5]/div[5]/div/div[5]/div[3]/ul/li[%d]/a"%r)
                    main_window = self.browser.current_window_handle
                    button.send_keys(Keys.CONTROL + Keys.RETURN)
                    self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
                    time.sleep(5)
                    self.browser.switch_to_window(main_window)


                    item["url"]=self.browser.current_url
                    time.sleep(10)

                    time.sleep(10)

                    self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                    self.browser.switch_to_window(main_window)

                    #item['model_link'] = site.xpath('//a[contains(@class,"{"na": !productClasses(product)}"]/@href').extract()[0]

                    yield item
