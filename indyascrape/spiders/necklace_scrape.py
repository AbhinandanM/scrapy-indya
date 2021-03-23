import scrapy
from ..items import IndyascrapeItem


class ItemScrape(scrapy.Spider):
    name = "Items"

    start_urls = ["https://www.houseofindya.com/zyra/necklace-sets/cat"]

    def parse(self, response):
        for item in response.css('#JsonProductList li'):
            yield{
                'product_name': item.css('li::attr(data-name)').get(),
                'product_price': item.css('li::attr(data-price)').get(),
                'product_img_url': item.css('li a img::attr(data-original)').get()
            }

    # An alternate way of scraping the same data

    '''def parse(self, response):
        item = IndyascrapeItem()

        Product_name = response.css(
            '#JsonProductList p').css('::text').extract_first()
        Price = response.css(
            '#JsonProductList span:nth-child(1)').css('::text').extract_first()
        Img_url = response.css('#JsonProductList .lazy').css(
            '::attr(data-original)').extract_first()

        item['product_name'] = Product_name
        item['product_price'] = Price
        item['product_img_link'] = Img_url

        yield item'''
