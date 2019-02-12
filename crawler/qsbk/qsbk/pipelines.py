# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

#class QsbkPipeline(object):
#    def __init__(self):
#        self.fp = open('duanzi.json','w',encoding='utf-8')

    #当爬虫打开的时候执行
#    def open_spider(self,spider):
#        print('爬虫开始了')

    #当爬虫有item传过来的时候被调用，ensure_ascii=False不设置的话无法导入中文
#    def process_item(self, item, spider):
#        item_json = json.dumps(dict(item),ensure_ascii=False)
#        self.fp.write(item_json+'\n')
#        return item

    #爬虫关闭时触发
#    def close_spider(self,spider):
#        print('爬虫结束了')

from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    #当爬虫打开的时候执行
    def open_spider(self,spider):
        print('爬虫开始了')

    #当爬虫有item传过来的时候被调用，ensure_ascii=False不设置的话无法导入中文
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    #爬虫关闭时触发
    def close_spider(self,spider):
        self.fp.close()
        print('爬虫结束了')