import scrapy


class GsmarenaSpider(scrapy.Spider):
    name = 'gsmarena'
    allowed_domains = ['www.gsmarena.com']
    start_urls = ['http://www.gsmarena.com/']

    def parse(self, response):
        pass
