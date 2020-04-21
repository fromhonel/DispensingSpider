# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class KmustItem(scrapy.Item):
    college = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    current_url = scrapy.Field()




class KmustDetailsItem(scrapy.Item):
    teacherName= scrapy.Field()
    gender= scrapy.Field()
    title= scrapy.Field()
    lineage= scrapy.Field()
    mail= scrapy.Field()
    phone= scrapy.Field()
    address= scrapy.Field()
    educationalBackground= scrapy.Field()
    researchDirection= scrapy.Field()
    profile= scrapy.Field()


class KmustInterestItem(scrapy.Item):
    teacherName= scrapy.Field()
    gender= scrapy.Field()
    title= scrapy.Field()
    lineage= scrapy.Field()
    mail= scrapy.Field()
    phone= scrapy.Field()
    address= scrapy.Field()
    educationalBackground= scrapy.Field()
    researchDirection= scrapy.Field()
    profile= scrapy.Field()