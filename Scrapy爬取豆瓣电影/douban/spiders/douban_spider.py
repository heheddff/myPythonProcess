# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        move_lists = response.xpath('//*[@id="content"]/div/div[1]/ol/li')

        for move_list in move_lists:
            douban_item = DoubanItem()
            douban_item['name'] = move_list.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            douban_item['number'] = move_list.xpath('./div/div[1]/em/text()').extract_first()
            douban_item['star'] = move_list.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            douban_item['evaluation'] = move_list.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            douban_item['description'] = move_list.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()
            instroduces = move_list.xpath('./div/div[2]/div[2]/p[1]/text()').extract()
            contents = ''
            for content in instroduces:
                contents += " ".join(content.strip().strip('\n').split())+" "
            douban_item['contents'] =contents
            yield douban_item
        next_link = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/link/@href').extract()
        #print(next_link)
        #pass
        if next_link:
            next_url = next_link[0]
            #使用urljoin构建绝对路径
            #next_url = response.urljoin(next_url)
            # yield scrapy.Request(next_link, callback=self.parse)
            #收到构建绝对路径
            #yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
            #response.follow方法使用相对路径
            #yield response.follow(next_url, callback=self.parse)
            #使用follow自动处理链接
            for href in next_link:
                print(href)
                yield response.follow(href,callback=self.parse)
