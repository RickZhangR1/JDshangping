# -*- coding: utf-8 -*-
import scrapy


class JdspSpider(scrapy.Spider):
    name = 'jdsp'
    allowed_domains = ['search.jd.com']
    start_urls = ['http://search.jd.com/']

    def parse(self, response):
        pass
