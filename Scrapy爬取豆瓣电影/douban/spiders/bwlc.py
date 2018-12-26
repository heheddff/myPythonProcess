# -*- coding: utf-8 -*-
import scrapy
from douban.items import BwlcItem

class BwlcSpider(scrapy.Spider):
    name = 'bwlc'
    allowed_domains = ['www.bwlc.net']
    start_urls = ['http://www.bwlc.net/bulletin/prevslto.html']
    #记录篮球出现的次数
    blue = {}
    #记录红球出现的次数
    red = {}
    def parse(self, response):
        #获取行记录
        trs = response.css('tr')
        for tr in trs[2:]:
            #获取单元格内容
            td = tr.css('td::text').extract()
            #蓝球自动加1
            self.blue[td[2]] = self.blue.get(td[2],0)+1
            bwc_item = BwlcItem()
            #期号
            bwc_item['period_number'] = td[0]
            #红球
            bwc_item['red'] = td[1]
            #蓝球
            bwc_item['blue'] = td[2]
            #日期
            bwc_item['date'] = td[4]
            #print(td[0],td[1],td[2],td[4])
            for i in td[1].split(','):
                #红球自动加1
                self.red[i] = self.red.get(i,0)+1
            yield  bwc_item
        #获取下一页链接
        next = response.xpath('//*[@id="lottery_tabs"]/div/div/a[3]/@href').extract_first()
        #生成决定url
        next = response.urljoin(next)
        if next:
            yield response.follow(next, callback=self.parse)
        #输出红球和篮球内容
        print(self.blue)
        print('red=>',self.red)