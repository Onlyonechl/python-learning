# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from autohome.items import AutohomeItem


class AutohomeSpiderSpider(CrawlSpider):
    name = 'autohome_spider'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/153.html']

    #元组形式，后面必须加一个逗号
    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/153.+'), callback='parse_page', follow=True),
    )


    def parse_item(self, response):
        pass


    def parse_page(self, response):
            category = response.xpath('//div[@class="uibox"]/div/text()').get()
            #这个class下面包含三个类，一个类用一个空格间隔开
            srcs = response.xpath('//div[contains(@class,"uibox-con")]/ul/li//img/@src').getall()
            srcs = list(map(lambda x:x.replace("t_",""),srcs))
            srcs = list(map(lambda x:response.urljoin(x),srcs))
            yield AutohomeItem(category=category,image_urls=srcs)
