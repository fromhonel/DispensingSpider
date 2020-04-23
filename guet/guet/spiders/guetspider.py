# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http.response.html import HtmlResponse
from guet.items import GuetItem


class GuetspiderSpider(scrapy.Spider):
    name = 'guetspider'
    allowed_domains = ['yjsgl.guet.edu.cn']
    start_urls = ['https://yjsgl.guet.edu.cn/Zs_shuoshiszsjz.aspx?nf=2020&dq_time']

    def parse(self, response):
        #//table[@class='tableTeacher'][3]/tbody/tr/td/table/tbody/tr[2]/td[1]  获取第一行第一列
        #//table[@class='tableTeacher'][3]/tbody/tr/td/table/tbody/tr[2]/td[2]  获取第一行第二列

        #//table[@class='tableTeacher'][3]/tbody/tr/td/table/tbody/tr[3]/td[1]
        #//table[@class='tableTeacher'][3]/tbody/tr/td/table/tbody/tr[3]/td[2]


        # //table[@class='tableTeacher'][3]/tbody/tr/td/table
        # major = response.xpath("//table[@class='tableTeacher'][3]/tbody/tr/td/table")
        # 当前只选择软件 计算机学院
    
        expect = "计算机与信息安全学院"

        recruitTables = response.xpath("//table[@class='tableTeacher']")
        for recruitTable in recruitTables:
            recruitCollege = recruitTable.xpath("./tbody/tr/td/table/caption//text()").get()
            tables  = recruitTable.xpath("./tbody/tr/td/table")
            if expect in recruitCollege:
                for table in tables:
                    trs = table.xpath("./tbody/tr")
                    for in_r,tr in enumerate(trs):
                        if in_r == 0:
                            continue
                        tds = tr.xpath("./td")
                        for in_d,td in enumerate(tds):
                            if in_d == 0:
                                major = td.xpath('./text()').getall()
                                print(major)
                            else:
                                professors_tr = td.xpath(".//tr")
                                for professor_tr in professors_tr:
                                    professor_td = professor_tr.xpath("./td")
                                    for professor in professor_td:
                                        href = professor.xpath("./a/@href").get()
                                        teacherName = professor.xpath("./a/text()").get()
                                        yield scrapy.Request(url=href,callback=self.parse_details,meta={"info":(recruitCollege,major,teacherName,href)},dont_filter=True)
                                        
                                    

                        
                    




    def parse_details(self, response):
        recruitCollege,major,teacherName,href = response.meta.get("info")
        def standard_info(info):
            if info is None:
                return ''
            if isinstance(info,str):
                info = info.strip()
            return info    
        item = {
            'recruitCollege':recruitCollege,
            'major':major,
            'teacherName':teacherName,
            'href':href,
            'position':'',
            'mail':'',
            'college':'',
            'researchDirection':'',
            'profile':'',
            'eduBackgroud':'',
            'workExperience':'',
            'honor':'',
            'paper':'',
            'work':'',
            'project':'',
            'propertyRight':'',
        }
        item['position'] = standard_info(response.xpath("//span[@id='scholarTitle']/text()").get())
        item['college'] =standard_info(response.xpath("//span[@id='scholarwork']/text()").get())
        item['researchDirection'] = standard_info(response.xpath("//span[@id='scholarField']/text()").get()) 
        panels = response.xpath('//div[@class="panel"]')
        for panel in panels:
            title = panel.xpath('.//div[@class="panel_title"]/text()').get().strip()
            temp = standard_info(panel.xpath('./div[@class="panel_content2"]//text()').getall()) 
            if "个人简介" in title:
              item['profile']  = temp
            elif "教育背景" in title:
               item['eduBackgroud']= temp
            elif "工作经历" in title:
               item['workExperience']= temp
            elif "主要荣誉" in title:
               item['honor'] = temp
            elif "主要论文" in title:
               item['paper'] = temp
            elif "学术著作" in title:
               item['work'] = temp
            elif "科研项目" in title:
               item['project'] = temp
            elif "知识产权" in title:
               item['propertyRight'] = temp
            elif "联系信息" in title:
               item['eamil'] = temp

        yield GuetItem(
                recruitCollege=item["recruitCollege"],
                major=item["major"],
                href=item["href"],
                teacherName=item["teacherName"],
                position=item["position"],
                mail=item["mail"],
                college=item["college"],
                researchDirection=item["researchDirection"],
                profile=item["profile"],
                eduBackgroud=item["eduBackgroud"],
                workExperience=item["workExperience"],
                honor=item["honor"],
                paper=item["paper"],
                work=item["work"],
                project=item["project"],
                propertyRight=item["propertyRight"],
            )
        
    


                


        
