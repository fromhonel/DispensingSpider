# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuetItem(scrapy.Item):
    recruitCollege= scrapy.Field()
    major= scrapy.Field()
    href= scrapy.Field()
    teacherName= scrapy.Field()
    position= scrapy.Field()
    mail=scrapy.Field()
    college=scrapy.Field()
    researchDirection=scrapy.Field()
    profile=scrapy.Field()
    eduBackgroud=scrapy.Field()
    workExperience=scrapy.Field()
    honor=scrapy.Field()
    paper=scrapy.Field()
    work=scrapy.Field()
    project=scrapy.Field()
    propertyRight=scrapy.Field()




class GuetInterestItem(scrapy.Item):
    teacherName= scrapy.Field()
    position= scrapy.Field()
    mail= scrapy.Field()
    phone= scrapy.Field()
    college= scrapy.Field()
    researchDirection= scrapy.Field()
    profile= scrapy.Field()
    eduBackgroud= scrapy.Field()
    workExperience= scrapy.Field()
    honor=  scrapy.Field()
    paper = scrapy.Field()
    work = scrapy.Field()
    project =  scrapy.Field()
    propertyRight =  scrapy.Field()
    contactInfo = scrapy.Field()