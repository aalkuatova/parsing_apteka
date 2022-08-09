import scrapy


class AptekaItem(scrapy.Item):
    high_category = scrapy.Field()
    small_category = scrapy.Field()
    name = scrapy.Field()
    sku = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    specification = scrapy.Field()
    image_urls = scrapy.Field()
    prod_link = scrapy.Field()
    image_link = scrapy.Field()
    
    
