# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 词条名称
    title = scrapy.Field()
    # 词条地址
    entry_href = scrapy.Field()
    # 词条简介
    content = scrapy.Field()
    # 开放分类 一级分类
    category_1 = scrapy.Field()
    # 开放分类 二级分类
    category_2 = scrapy.Field()
    data = scrapy.Field()
