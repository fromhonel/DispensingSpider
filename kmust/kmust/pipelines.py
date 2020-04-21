# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html




from scrapy.exporters import JsonLinesItemExporter
from kmust.items import KmustItem,KmustDetailsItem,KmustInterestItem

class KmustPipeline(object):
    def __init__(self):
        self.all_info_fp = open("info.json","wb")
        self.information_fp = open("information.json","wb")
        self.interest_fp = open("interest.json","wb")
        self.info_exporter = JsonLinesItemExporter(self.all_info_fp,ensure_ascii=False)
        self.information_exporter = JsonLinesItemExporter(self.information_fp,ensure_ascii=False)
        self.interest_exporter = JsonLinesItemExporter(self.interest_fp,ensure_ascii=False)


    def process_item(self, item, spider):
        if isinstance(item, KmustItem):
            self.info_exporter.export_item(item)
        elif isinstance(item,KmustDetailsItem):
            self.information_exporter.export_item(item)
        else:
            self.interest_exporter.export_item(item)
        return item
    
    def close_spider(self,spider):
        if isinstance(item, KmustItem):
            self.all_info_fp.close()
        elif isinstance(item,KmustDetailsItem):
            self.information_fp.close()
        else:
            self.interest_fp.close()
