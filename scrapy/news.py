import scrapy
from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        print(response.css('ul.topics a::attr("href")').extract())