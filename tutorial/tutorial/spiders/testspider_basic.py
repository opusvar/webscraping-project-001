import scrapy


class TestspiderBasicSpider(scrapy.Spider):
    name = 'testspider_basic'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']
    
    def start_requests(self):
        urls = ["http://example.com/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        pass
