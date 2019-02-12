# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    #省份
    province = scrapy.Field()
    #城市
    city = scrapy.Field()
    #行政区
    district = scrapy.Field()
    #楼盘名称
    name = scrapy.Field()
    #价格
    price = scrapy.Field()
    #户型
    rooms = scrapy.Field()
    #面积
    area = scrapy.Field()
    #地址
    address = scrapy.Field()
    #是否在售
    sale = scrapy.Field()
    #详情页面链接
    origin_url = scrapy.Field()

class ESFHouseItem(scrapy.Item):
    #省份
    province = scrapy.Field()
    #城市
    city = scrapy.Field()
    #行政区
    district = scrapy.Field()
    #小区名称
    name = scrapy.Field()
    #总价
    price = scrapy.Field()
    #单价
    unit = scrapy.Field()
    #户型
    rooms = scrapy.Field()
    #楼层
    floor = scrapy.Field
    #面积
    area = scrapy.Field()
    #朝向
    toward = scrapy.Field()
    #年份
    year = scrapy.Field()
    #地址
    address = scrapy.Field()
    #详情页面链接
    origin_url = scrapy.Field()