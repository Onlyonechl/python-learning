# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    avatar = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    words_count = scrapy.Field()
    content = scrapy.Field()
    article_id = scrapy.Field()
    views_count = scrapy.Field()
    comments_count = scrapy.Field()
    likes_count = scrapy.Field()
    subjects = scrapy.Field()