# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from JobboleArticle.items import TXTitem
import re
import datetime

class TXTspider(scrapy.Spider):
    name = 'TXTspider'
    allowed_domains = ['528h = =低调']
    start_urls = ['...']

    def parse(self, response):
        post_nodes = response.css(".post a::attr(href)").extract()
        for post_node in post_nodes:
            yield Request(parse.urljoin(response.url, post_node), callback=self.parse_detail)

        for i in range(2,40):
            next_page_url = "528h低调"+str(i)
            if next_page_url:
                yield Request(parse.urljoin(response.url, next_page_url), callback=self.parse)

    def parse_detail(self, response):
        # title, author, fav_numbers, url, content, date, tags
        item = TXTitem()
        item["title"] = response.css(".post h2::text").extract_first("").strip()
        sentence_list = response.css(".entry p::text").extract()
        sentence_list = [i.strip(' \t\n\r') for i in sentence_list]
        sentence_list = [i for i in sentence_list if not i.strip()==""]
        strs = ""
        for str in sentence_list:
            strs += str
        item["content"] = [strs]
        yield item
