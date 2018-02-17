# -*- coding: utf-8 -*-
import scrapy


class BolespiderSpider(scrapy.Spider):
    name = 'BoleSpider'
    allowed_domains = ['http://www.importnew.com/all-posts']
    start_urls = ['http://http://www.importnew.com/all-posts/']

    def parse(self, response):
        pass
