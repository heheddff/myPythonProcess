# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#豆瓣电影
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    number = scrapy.Field()
    star = scrapy.Field()
    evaluation = scrapy.Field()
    description = scrapy.Field()
    contents = scrapy.Field()

#双色球
class BwlcItem(scrapy.Item):
    period_number = scrapy.Field()
    red = scrapy.Field()
    blue = scrapy.Field()
    date = scrapy.Field()
