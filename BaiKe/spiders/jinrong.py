# -*- coding: utf-8 -*-
import scrapy

from BaiKe.items import BaikeItem


class JinrongSpider(scrapy.Spider):
    name = 'jinrong'
    allowed_domains = ['http://baike.baidu.com']
    # start_urls = ['http://baike.baidu.com/fenlei/%E9%87%91%E8%9E%8D']  #  金融
    # start_urls = ['http://baike.baidu.com/fenlei/%E7%BB%8F%E6%B5%8E%E5%AD%A6']  # 经济学
    start_urls = ['http://baike.baidu.com/fenlei/%E8%82%A1%E7%A5%A8']  # 股票

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
            yield scrapy.Request(url="http://baike.baidu.com" + item['entry_href'], meta={'item': item},
                                 callback=self.get_data,
                                 dont_filter=True)  # 爬取城市详情

        # have_next = response.xpath('//*[@id="next"]')
        # if have_next:
        #     fenlei_url = 'http://baike.baidu.com/fenlei/'
        #     next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        #     yield scrapy.Request(fenlei_url + str(next_url), callback=self.parse, dont_filter=True)

    def get_data(self, response):
        item = response.meta['item']._values
        div = response.xpath('//div[@class="basic-info cmn-clearfix"]')[0]
        # dts = div.xpath('.//dl/dt')
        # dds = div.xpath('.//dl/dd')
        dts = div.xpath('//dt[contains(@class,"basicInfo-item name")]/text()').extract()
        dds = div.xpath('//dd[contains(@class,"basicInfo-item value")]')

        dic = {}
        for i, dt in enumerate(dts):
            # t_dt = dt.xpath('//text()')
            # key =''.join(t_dt).replace('\n', '').strip()
            key=''.join(dt.split())
            value = dds[i].xpath('.//text()|.//a/text()').extract()
            # t_value = ''.join(value).replace('\n', '').strip()
            # print(i)
            # print(dds[i])
            dic[key] = ''.join(value).replace('\n', '').strip()
        item['date'] = dic
        print(dic)
        yield item
