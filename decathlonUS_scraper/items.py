import scrapy


class DecathlonusScraperItem(scrapy.Item):
    category = scrapy.Field()
    brand = scrapy.Field()
    product_name = scrapy.Field()
    star_rating = scrapy.Field()
    reviews = scrapy.Field()
    all_description = scrapy.Field()
    product_ids = scrapy.Field()
    colors = scrapy.Field()
    sizes = scrapy.Field()
    regular_prices = scrapy.Field()
    previous_price = scrapy.Field()
    feature_img = scrapy.Field()
    carousel_img = scrapy.Field()
    url = scrapy.Field()
