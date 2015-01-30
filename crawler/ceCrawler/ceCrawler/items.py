# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class courseItem(scrapy.Item):
	courseID=scrapy.Field()
	courseName=scrapy.Field()
	teacher=scrapy.Field()
	TA=scrapy.Field()
	link=scrapy.Field()

