# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from pymysql import cursors
from scrapy1 import settings
from twisted.enterprise import adbapi


class Scrapy1Pipeline(object):
    def process_item(self, item, spider):
        return item


class DoubanPipeline(object):

    # 初始化函数
    def __init__(self, db_pool):
        self.db_pool = db_pool

    # 从settings配置文件中读取参数
    @classmethod
    def from_settings(cls, settings):
        # 用一个db_params接收连接数据库的参数
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            database=settings['MYSQL_DBNAME'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True,
            # 设置游标类型
            cursorclass=cursors.DictCursor
        )
        # 创建连接池
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)

        # 返回一个pipeline对象
        return cls(db_pool)

    # 处理item函数
    def process_item(self, item, spider):
        # 把要执行的sql放入连接池
        query = self.db_pool.runInteraction(self.insert_into, item)
        # 如果sql执行发送错误,自动回调addErrBack()函数
        query.addErrback(self.handle_error, item, spider)

        # 返回Item
        return item

    # 处理sql函数
    def insert_into(self, cursor, item):
        # 创建sql语句
        sql = "INSERT INTO test (no,name,info,star,num,introduce) VALUES (%s,%s,%s,%s,%s,%s)"
        # 暂存数据
        no = item['no']
        name = item['name']
        info = item['info']
        star = item['star']
        num = item['num']
        introduce = item['introduce']
        # 把数据放进data
        data = (no, name, info, star, num, introduce)
        # 执行sql语句
        cursor.execute(sql, data)
        # Testing SQL Syntax
        print(sql)
        # 错误函数

    def handle_error(self, failure, item, spider):
        # #输出错误信息
        print(failure)


# 写这个管道时，遇到了点麻烦，sql语句一直报错，最后是加了`这个符号解决了。2019.5.12.母亲节快乐
class ClubPipeline(object):

    # 初始化函数
    def __init__(self, db_pool):
        self.db_pool = db_pool

    # 从settings配置文件中读取参数
    @classmethod
    def from_settings(cls, settings):
        # 用一个db_params接收连接数据库的参数
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            database=settings['MYSQL_DBNAME'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True,
            # 设置游标类型
            cursorclass=cursors.DictCursor
        )
        # 创建连接池
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)

        # 返回一个pipeline对象
        return cls(db_pool)

    # 处理item函数
    def process_item(self, item, spider):
        # 把要执行的sql放入连接池
        query = self.db_pool.runInteraction(self.insert_into, item)
        # 如果sql执行发送错误,自动回调addErrBack()函数
        query.addErrback(self.handle_error, item, spider)

        # 返回Item
        return item

    # 处理sql函数
    def insert_into(self, cursor, item):
        # 创建sql语句
        sql = "INSERT INTO premier (`rank`,`name`,`turn`,`win`,`tie`,`lose`,`goals`,`fumble`,`delt`,`score`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # 暂存数据
        rank = item['rank']
        name = item['name']
        turn = item['turn']
        win = item['win']
        tie = item['tie']
        lose = item['lose']
        goals = item['goals']
        fumble = item['fumble']
        delt = item['delt']
        score = item['score']

        # 把数据放进data
        data = (rank, name, turn, win, tie, lose, goals, fumble, delt, score)
        # 执行sql语句
        cursor.execute(sql, data)
        # Testing SQL Syntax
        print('===>' + sql)
        # 错误函数

    def handle_error(self, failure, item, spider):
        # #输出错误信息
        print(failure)


"""
# 之前一直使用的是 MySQL 数据库，今天试一下 MongoDB，存的是英超联赛之前赛季的数据
# 2019.10.15
# 需要使用 mongoDB 的时候
    1.取消 settings.py 中开通 MongoDBPipeline 的注释;
    2.更改 self.collection = self.db['bus'] 中的表名;
    3.当前使用的是 England 数据库,如需更换请前往settings.py更换.
"""
class MongoDBPipeline(object):

    def __init__(self, host, port, dbname):
        self.host = host
        self.port = port
        self.dbname = dbname

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # localhost
            host = crawler.settings.get('MONGODB_HOST'),
            # MongoDB 的端口
            port = crawler.settings.get('MONGODB_PORT'),
            # 要链接的数据库
            dbname = crawler.settings.get('MONGODB_DBNAME'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client[self.dbname]
        # 表(collection),使用时请更换!
        self.collection = self.db['bus']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert(data)
        return item
