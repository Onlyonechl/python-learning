# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    #爬虫的名字，名字必须是唯一的。
    name = 'qsbk_spider'
    #允许的域名。爬虫只会爬取这个域名下的网页，其他不是这个域名下的网页会被自动忽略。
    allowed_domains = ['qiushibaike.com']
    #爬虫从这个变量中的url开始。
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = 'https://www.qiushibaike.com'

    #引擎会把下载器下载回来的数据扔给爬虫解析，爬虫再把数据传给这个parse方法。这个是个固定的写法。这个方法的作用有两个，第一个是提取想要的数据。第二个是生成下一个请求的url。
    def parse(self, response):
        # SelectorList对象
        duanzidivs = response.xpath('//div[@id="content-left"]/div')
        for duanzidiv in duanzidivs:
            # Selector
            # get方法获取的是Selector中的第一个文本，返回的是str类型
            author = duanzidiv.xpath('.//h2/text()').get().strip()
            # getall方法获取Selector中所有的文本，返回的是一个列表
            content = duanzidiv.xpath('.//div[@class="content"]//text()').getall()
            content = ''.join(content).strip()

            item = QsbkItem(author=author,content=content)
            #用yield生成器逐个返回item给pipelines
            yield item
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if not next_url:
            return
        else:
            #callback=self.parse是回调给parse函数
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)