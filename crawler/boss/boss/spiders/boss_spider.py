# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlS
from scrapy import

class BossSpiderSpider(CrawlSpider):
    name = 'boss_spider'
    allowed_domains = ['zhipin.com']
    start_urls = ['http://zhipin.com/']

    rules = (
        #爬取列表页
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
