# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import os
import json
import codecs

project_dir = os.path.abspath(os.path.dirname(__file__))
contents_store = os.path.join(project_dir, 'contents')

class JobbolearticlePipeline(object):
    def process_item(self, item, spider):
        file = codecs.open(contents_store+"/"+item.get("title")+".txt", 'w+', encoding="utf-8")
        lines = json.dumps(dict(item), ensure_ascii=False)
        file.write(lines)
        file.close()
        return item

