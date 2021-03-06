import scrapy
import re
from ceCrawler.items import courseItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
def first ():
	firstYear=79
	lastYear=94
	ret=[]	
	for i in range (firstYear,lastYear):
		ret.append("http://ce.sharif.ir/courses/"+str(i)+"-"+str(i+1)+"/1")
		ret.append("http://ce.sharif.ir/courses/"+str(i)+"-"+str(i+1)+"/2")
	ret.append('http://ce.sharif.edu/courses/84-85/summer/')	
	return ret

class DmozSpider(scrapy.Spider):
    name = "ceCrawl"
    allowed_domains = ["http://ce.sharif.ir"]
    start_urls = first()
    def parse(self, response):
		persons=response.xpath('//table/tr/td[contains (@valign,"top") and not(contains(@align,"right"))]')
		courses=response.xpath('//td[contains(@class, "tableHead2")]')
		for index,person in enumerate(persons):
			item=courseItem()
			item["link"]= courses[index].xpath('./a/@href').extract()[0]
			courseLine=courses[index].xpath('./a/text()').extract()[0]
			courseLine=courseLine.replace('-','')
			item["courseID"]=courseLine[0:5]
			item["courseName"]=courseLine[6:]
			pText=person.extract()
			pText=re.sub(r'<a href="(.+?)">','',pText)
			if pText.find('+')!=-1 and pText.find('/')!=-1:
				teacher=pText[pText.index('+')+1:pText.index('/')-1]
				item["teacher"]=teacher.replace('\n','').strip()
			
			yield item



