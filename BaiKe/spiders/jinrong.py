# -*- coding: utf-8 -*-
import scrapy

from BaiKe.items import BaikeItem


class JinrongSpider(scrapy.Spider):
    name = 'jinrong'
    allowed_domains = ['http://baike.baidu.com']
    start_urls = ['http://baike.baidu.com/fenlei/%E9%87%91%E8%9E%8D']

    # 编写爬取方法
    def parse(self, response):
        for line in response.xpath('//div[@class="list"]'):
            # 初始化item对象保存爬取的信息
            item = BaikeItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['title'] = line.xpath(
                './/a/text()').extract_first()
            item['entry_href'] = line.xpath(
                './/a/@href').extract_first()
            item['content'] = line.xpath(
                './/p/text()').extract_first()
            item['category_1'] = line.xpath(
                './/div/a[1]/text()').extract_first()
            item['category_2'] = line.xpath(
                './/div/a[2]/text()').extract_first()
            yield item

        have_next = response.xpath('//*[@id="next"]')
        if have_next:
            fenlei_url = 'http://baike.baidu.com/fenlei/'
            next_url = response.xpath('//*[@id="next"]/@href').extract_first()
            yield scrapy.Request(fenlei_url + str(next_url), callback=self.parse, dont_filter=True)
