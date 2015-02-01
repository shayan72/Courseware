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
class course(scrapy.Item):
	link=scrapy.Field()
	name=scrapy.Field()
	term=scrapy.Field()
	group=scrapy.Field()
	professors=scrapy.Field()
	teacher_assistants=scrapy.Field()
	description=scrapy.Field()
	picture=scrapy.Field()
	credit=scrapy.Field()
	textBook=scrapy.Field()
class announcments(scrapy.Item):
	link=scrapy.Field()
	annons=scrapy.Field()	
class assignment(scrapy.Item):
	link=scrapy.Field()
	HWlink=scrapy.Field()
	Deadline=scrapy.Field()
	name=scrapy.Field()
