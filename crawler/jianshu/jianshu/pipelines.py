# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


"""
class JianshuPipeline(object):
    def __init__(self):
        dbparams = {
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'root',
            'database':'jianshu',
            'charset':'utf8'
        }

        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],
                                      item['article_id'],item['words_count']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = ""
            insert into article(id,title,content,author,avatar,pub_time,article_id,words_count) values(null,%s,%s,%s,
            %s,%s,%s,%s)
            ""
            return self._sql
        return self._sql

"""

#Twisted异步存储到数据库
class JianShuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'root',
            'database':'jianshu',
            'charset':'utf8',
            'cursorclass':cursors.DictCursor
        }

        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        cursor.execute(self.sql, (
        item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['article_id'],
        item['words_count'],item['views_count'],item['comments_count'],item['likes_count'],item['subjects']))

    def handle_error(self,error,item,spider):
        print('='*10+'error'+'='*10)
        print(error)
        print('='*10+'error'+'='*10)

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,title,content,author,avatar,pub_time,article_id,words_count,views_count,
            likes_count,comments_count,subjects
            ) values(null,
            %s,                        %s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql