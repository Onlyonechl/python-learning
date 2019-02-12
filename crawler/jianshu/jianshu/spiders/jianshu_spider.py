# -*- coding: utf-8 -*-

import scrapy

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from jianshu.items import JianshuItem

class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//h1[@class="title"]/text()').get()
        avatar = response.xpath('//a[@class="avatar"]/img/@src').get()
        author = response.xpath('//span[@class="name"]/a/text()').get()
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get().replace("*","")
        words_count = response.xpath('//span[@class="wordage"]/text()').get().split(" ")[1]
        content = response.xpath('//div[@class="show-content-free"]').get()
        article_id = (response.url.split('?')[0]).split('/')[-1]

        views_count = response.xpath('//span[@class="views-count"]/text()').get().split(" ")[1]
        comments_count = response.xpath('//span[@class="comments-count"]/text()').get().split(" ")[1]
        likes_count = response.xpath('//span[@class="likes-count"]/text()').get().split(" ")[1]
        subjects = ','.join(response.xpath('//div[@class="include-collection"]/a/div/text()').getall())

        item = JianshuItem(
            title = title,
            avatar = avatar,
            author = author,
            pub_time = pub_time,
            words_count = words_count,
            content = content,
            article_id = article_id,
            views_count = views_count,
            comments_count = comments_count,
            likes_count = likes_count,
            subjects = subjects
        )
        yield item