import scrapy

class testSpider(scrapy.Spider):
    name = 'tests'
    
    start_urls = [
        'https://omniabrush.com/collections/individual-brushes',
    ]
    
    def parse(self, response):
        for listItem in response.xpath("//li[@class='product-item']"):
            yield {
                'Product Title': listItem.xpath("div[@class='product-title']/a/text()")[1].getall(),
                'Link Title': listItem.xpath("div[contains(@class, 'product-card')]/a[starts-with(@href, '/collections/individual-brushes/products/')]/@title").getall(),
                'Page Number': listItem.xpath("//span[contains(@class, 'current')]/text()").get(),
                }
            
        next_page = response.css("span.next a::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
