import scrapy

class Headline(scrapy.Item):
	title = scrapy.Field()
	body = scrapy.Field()

item = Headline()
item['title'] = 'Example'
print(item['title'])
