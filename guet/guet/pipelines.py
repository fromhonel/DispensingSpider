# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy.exporters import JsonLinesItemExporter
from guet.items import GuetItem,GuetInterestItem

class GuetPipeline(object):
    def __init__(self):
        self.information_fp = open("information.json","wb")
        self.interest_fp = open("interest.json","wb")
        self.information_exporter = JsonLinesItemExporter(self.information_fp,ensure_ascii=False)
        self.interest_exporter = JsonLinesItemExporter(self.interest_fp,ensure_ascii=False)


    def process_item(self, item, spider):
        if isinstance(item, GuetItem):
            self.information_exporter.export_item(item)
        else:
            self.interest_exporter.export_item(item)
        return item
    
    def close_spider(self,spider):
        self.information_fp.close()
        self.interest_fp.close()
