# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewHouseItem,ESFHouseItem
from scrapy_redis.spiders import RedisSpider

class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    #start_urls = ['http://www.fang.com/SoufunFamily.htm']
    redis_key = 'fang:start_urls'

    def parse(self, response):
        trs = response.xpath('//div[@class="outCont"]//tr')
        province = None
        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')
            province_td = tds[0]
            province_text = province_td.xpath('.//text()').get()
            province_text = re.sub(r'\s','',province_text)
            if province_text:
                province = province_text

            #不爬取海外房源
            if province == '其它':
                continue

            city_td = tds[1]
            city_links = city_td.xpath('.//a')
            for city_link in city_links:
                city = city_link.xpath('.//text()').get()
                city_url = city_link.xpath('.//@href').get()
                #构建新房和二手房的url链接
                url_module = city_url.split('//')
                scheme = url_module[0]
                domain = url_module[1]
                if 'bj.' in domain:
                    newhouse_url = 'http://newhouse.fang.com/house/s/'
                    esf_url = 'http://esf.fang.com/'
                else:
                    newhouse_url = scheme + '//newhouse.' + domain + 'house/s/'
                    esf_url = scheme + '//esf.' + domain

                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={'info':(province,city)})
                yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={'info':(province,city)})

    def parse_newhouse(self,response):
        province,city = response.meta.get('info')
        nlc_details = response.xpath('//div[@class="nlc_details"]')
        for nlc_detail in nlc_details:
            name = nlc_detail.xpath('.//div[@class="nlcd_name"]/a/text()').get().strip()
            house_type_list = nlc_detail.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
            #house_type_list = list(map(lambda x:re.sub(r'\s','',x),house_type_list))
            rooms = list(filter(lambda x:x.endswith('居'),house_type_list))
            area = ''.join(nlc_detail.xpath('.//div[contains(@class,"house_type")]/text()').getall())
            area = re.sub(r'\s|－|/','',area)
            address = nlc_detail.xpath('.//div[@class="address"]/a/@title').get()
            district_text = ''.join(nlc_detail.xpath('.//div[@class="address"]/a//text()').getall())
            district = re.search(r'.*\[(.+)\].*',district_text).group(1)
            sale = nlc_detail.xpath('.//div[contains(@class,"fangyuan")]/span/text()').get()
            price = ''.join(nlc_detail.xpath('.//div[@class="nhouse_price"]//text()').getall())
            price = re.sub(r'\s|广告','',price)
            origin_url = nlc_detail.xpath('.//div[@class="nlcd_name"]/a/@href').get()

            item = NewHouseItem(name=name,rooms=rooms,area=area,address=address,district=district,sale=sale,
                                price=price,origin_url=origin_url,province=province,city=city)

            yield item

        next_url = response.xpath('//a[@class="next"]/@href').get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_newhouse,meta={'info':(province,city)})


    def parse_esf(self,response):
        province,city = response.meta.get('info')
        dls = response.xpath('//dl[@dataflag="bag"]')
        for dl in dls:
            name = dl.xpath('.//p[@class="add_shop"]/a/@title').get()
            address = dl.xpath('.//p[@class="add_shop"]/span/text()').get()
            infos = dl.xpath('.//p[@class="tel_shop"]/text()').getall()
            rooms = infos[0].strip()
            area = infos[1].strip()
            floor = infos[2].strip()
            forward = infos[3].strip()
            year = infos[4].strip()
            price = ''.join(dl.xpath('.//dd[@class="price_right"]/span[1]//text()').getall())
            unit = dl.xpath('.//dd[@class="price_right"]/span[1]//text()').get()
            origin_url = dl.xpath('.//a[@target="_blank"]/@href').get()
            origin_url = response.urljoin(origin_url)
            item = ESFHouseItem(name=name,rooms=rooms,area=area,address=address,district=district,price=price,unit=unit,floor=floor,forward=forward,year=year,origin_url=origin_url,province=province,city=city)
            yield item

        text = response.xpath('//div[@class="page_al"]/a[12]/text()').get()
        if text == "下一页":
            next_url = response.xpath('//div[@class="page_al"]/a[12]/@href').get()
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_esf,meta={'info':(province,city)})
