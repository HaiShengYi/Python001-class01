import scrapy

class SpidersItem(scrapy.Item):
    # 电影名称、电影类型和上映时间
    name = scrapy.Field()
    type = scrapy.Field()
    time = scrapy.Field()
