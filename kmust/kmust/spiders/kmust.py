# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http.response.html import HtmlResponse
from kmust.items import KmustItem,KmustDetailsItem,KmustInterestItem


class KmustSpider(scrapy.Spider):
    name = 'kmust'
    allowed_domains = ['http://school.freekaoyan.com']
    start_urls = ['http://school.freekaoyan.com/yunnan/kmust/daoshi/']

    def parse(self, response):
        current_url = response.request.url
        lis = response.xpath("//div[@class='list2']//li");
        for li in lis:
            title = li.xpath("./h5/a/text()").get();
            href = li.xpath("./h5/a/@href").get();
            if "排序" not in title:
                mentorInfo = re.match( r'昆明理工大学(.*)研究生导师简介-(.*)', title, re.M)
                if mentorInfo:
                    tutor_info={
                        'college':mentorInfo.group(1),
                        'name':mentorInfo.group(2),
                        'title':title,
                        'href':href,
                        'current_url':current_url
                    }
                else:
                    tutor_info={
                        'college':"",
                        'name':"",
                        'title':title,
                        'href':href,
                        'current_url':current_url
                    }   
                yield KmustItem(college=tutor_info['college'],name=tutor_info['name'],title=tutor_info['title'],href=tutor_info['href'],current_url=tutor_info['current_url'])
                if "信息工程与自动化学院" in tutor_info['college']:
                    yield scrapy.Request(url=href,callback=self.parse_details,dont_filter=True)
            else:
                continue
        next_pages = response.xpath("//div[@class='epages']//a")

        for next_page in next_pages:
            next_text = next_page.xpath('./text()').get()
            if '下一页' in next_text:
                next_url = next_page.xpath('./@href').get()
                yield scrapy.Request(url=next_url,callback=self.parse,dont_filter=True)
                break
            else:
                continue
        


        


    def parse_details(self,response):
        item = {'teacherName':"",'gender':"", 'title':"", 'lineage':"",'mail':"", 'phone':"",'address':"",'educationalBackground':"",'researchDirection':"",'profile':""}
        bs = response.xpath("//div[@class='content']//text()");
        i = 2
        for k in item:
            item[k] = bs[i].get()
            i += 2
        
        yield KmustDetailsItem(teacherName=item['teacherName'],gender=item['gender'],title=item['title'],lineage=item['lineage'],
        mail=item['mail'],phone=item['phone'],address=item['address'],educationalBackground=item['educationalBackground'],researchDirection=item['researchDirection'],
        profile=item['profile'])

        #  设置自己感兴趣的内容
        personalInterest = "网络"

        if personalInterest in item['researchDirection']:
            yield KmustInterestItem(teacherName=item['teacherName'],gender=item['gender'],title=item['title'],lineage=item['lineage'],
            mail=item['mail'],phone=item['phone'],address=item['address'],educationalBackground=item['educationalBackground'],researchDirection=item['researchDirection'],
            profile=item['profile'])
        

        



