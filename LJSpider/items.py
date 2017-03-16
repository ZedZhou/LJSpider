# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class LjspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LJItem(scrapy.Item):

    city_area = Field()
    brief = Field()
    price = Field()
    house_area = Field()
    house_room = Field()
    house_addr = Field()
    house_unit_price = Field()
    # 某房的url地址作为MongoDB唯一_id
    _id = Field()