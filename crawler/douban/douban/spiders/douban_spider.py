# -*- coding: utf-8 -*-
import scrapy
from PIL import Image
from urllib import request
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']
    login_url = 'https://accounts.douban.com/login'

    def parse(self, response):
        formdata = {
            'sourec':'None',
            'redir':'https://www.douban.com',
            'form_email':'562921525@qq.com',
            'form_password':'chl930528',
            'login':'登录'
        }

        captcha_url = response.xpath('//img[@id="captcha_image"]/@src').get()
        print('='*30)
        print(captcha_url)
        if captcha_url:
            captcha = self.regonize_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath('//input[@name="captcha_id"]/@value').get()
            formdata['captcha-id'] = captcha_id


    class MM(DoubanItem):
