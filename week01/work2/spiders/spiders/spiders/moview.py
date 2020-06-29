import scrapy

from spiders.items import SpidersItem

class MoviewSpider(scrapy.Spider):
    name = 'moview'
    allowed_domains = ['https://maoyan.com/']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        moview = SpidersItem()
        dl = response.xpath('//div[@class="movie-item-hover"]')
        type(dl)
        for dd in dl:
            # 电影名称
            moview["name"] = "".join(dd.xpath('./a/div/div[1]/span[1]/text()').extract()[0])
            # # 电影类型
            moview["type"] = "".join(dd.xpath('./a/div/div[2]/text()').extract()[1]).strip()
            # 上映时间
            moview["time"] = "".join(dd.xpath('./a/div/div[4]/text()').extract()[1]).strip()
            # 返回
            yield moview
