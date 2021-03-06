# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobbolearticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title, author, fav_numbers, url, md5_url, content, date, tags
    title = scrapy.Field()
    author = scrapy.Field()
    fav_numbers = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()
    pass

class TXTitem(scrapy.Item):
    content = scrapy.Field()
    title = scrapy.Field()