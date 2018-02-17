# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from JobboleArticle.items import JobbolearticleItem
import re
import datetime

class BolespiderSpider(scrapy.Spider):
    name = 'BoleSpider'
    allowed_domains = ['python.jobbole.com']
    start_urls = ['http://python.jobbole.com/all-posts/']

    def parse(self, response):
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(parse.urljoin(response.url, post_url), callback=self.parse_detail)

        next_page_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_page_url:
            yield Request(parse.urljoin(response.url, next_page_url),callback=self.parse)

    def parse_detail(self, response):
        # title, author, fav_numbers, url, content, date, tags
        item = JobbolearticleItem()
        item["title"] = response.css(".entry-header h1::text").extract_first("")
        item["author"] = response.css(".copyright-area a::text").extract_first("")
        item["url"] = response.url

        fav_numbers = response.css(".vote-post-up h10::text").extract_first("")
        item["fav_numbers"] = 0 if fav_numbers == "" else int (fav_numbers)
        item["content"] = response.css("div.entry").extract_first("")
        date_string = response.css(".entry-meta p::text").extract_first("")
        date_time = date_string.strip().replace("·","").strip()
        item["date"] = date_time

        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        item["tags"] = tags
        yield item

