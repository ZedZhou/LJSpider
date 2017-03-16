# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .items import LJItem
from scrapy.exceptions import DropItem


class MongoPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['lianjia']
        self.house_info = db['house_info']
    def process_item(self, item, spider):

        if isinstance(item,LJItem):
            try:
                self.house_info.insert(dict(item))
                print('保存成功！！！')
            except Exception as e:
                print('过滤重复Item')
        return item
