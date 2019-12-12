# -*- coding: utf-8 -*-
import scrapy
from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        for url in response.css('ul.topics a::attr("href")').re(r'/pickup/\d+$'):
        	yield scrapy.Request(response.urljoin(url), self.parsde_topics)

    def parase_topics(self, response):
    	item = Headline()
    	item['title'] = response.css('.hbody').xpath('string()').extract_first()
    	yield item