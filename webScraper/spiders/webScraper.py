import scrapy

class testSpider(scrapy.Spider):
    name = 'tests'

    start_urls = [
        'https://omniabrush.com/collections/individual-brushes?sort_by=best-selling',
    ]

    def parse(self, response):
        for listItem in response.xpath("//li[@class='product-item']"):
            
            productTitle = listItem.xpath("div[@class='product-title']/a/text()")[1].getall()
            
            linkTitle = listItem.xpath("div[contains(@class, 'product-card')]/a[starts-with(@href, '/collections/individual-brushes/products/')]/@title").getall()
            
            pageNumber = listItem.xpath("//span[contains(@class, 'current')]/text()").get()

            yield {
                'Product Title': productTitle[0].strip(),
                'Link Title': linkTitle[0].strip(),
                'Page Number': pageNumber[0].strip(),
            }

        next_page = response.css("span.next a::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
