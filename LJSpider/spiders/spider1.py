# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import LJItem
import random

class Spider1Spider(RedisSpider):
    name = "redisspider"
    allowed_domains = ["www.lianjia.com"]
    redis_key = 'lianjia_beijing_urls'

    custom_settings = {
        'DOWNLOAD_DELAY':random.randint(1, 4)+random.random()
    }

    def parse(self, response):
        """
    city_area = Field()
    brief = Field()
    price = Field()
    house_area = Field()
    house_room = Field()
    house_addr = Field()
    house_unit_price = Field()

        """

        res = response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]')
        for i in res:
            try:
                item = LJItem()
                item['brief'] = i.xpath('div[@class="title"]/a/text()').extract_first()
                item['price'] = i.xpath('//div[@class="totalPrice"]/span/text()').extract_first()
                item['house_area'] = i.xpath('div[@class="address"]/div[@class="houseInfo"]/text()').extract_first().strip().split('|')[2].strip()[:-2]
                item['house_room'] = i.xpath('div[@class="address"]/div[@class="houseInfo"]/text()').extract_first().strip().split('|')[1].strip()
                item['house_unit_price'] = i.xpath('//div[@class="unitPrice"]/span/text()').extract_first()[2:-4]
                item['house_addr'] = i.xpath('div[@class="address"]/div[@class="houseInfo"]/a/text()').extract_first()
                item['city_area'] = response.url.split('/')[-3]
                item['_id'] = i.xpath('div[@class="title"]/a/@href').extract_first()
            except Exception as e:
                print(e)
            yield item