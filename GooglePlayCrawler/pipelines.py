# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem


class GooglePlayCrawlerPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient('127.0.0.1', 27017)
        db = connection['GoogleApp']
        self.collection = db['GooglePlayCrawler']

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing{0}!'.format(data))
        if valid:
            self.collection.insert(dict(item))

        return item
