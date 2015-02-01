import scrapy
import lxml.html
import re
import urllib2
from ceCrawler.items import assignment
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import json
def first():
    list=[]
    with open("/home/babak/Dropbox/semesters/7/tahlil/project/scrapy/ceCrawler/new.json",'r') as f:
        for line in f:
			line=line.strip()
			list.append( json.loads(line)['link']+"/index.php/section/assignments/file/assignments")
    return list


class DmozSpider(scrapy.Spider):
    name = "assignmentCrawler"
    allowed_domains = ["http://ce.sharif.ir"]
    start_urls = first()
    def parse(self, response):
		hxs = Selector(response)
		item=assignment()
		item['link']=response.url.replace('/index.php/section/assignments/file/assignments','')
		dateSplitter="||||||||||" #10 ta \
		anonsSplitter="**********" #10 ta *
		name=""
		date=''
		HWlink=''
		for i,x in enumerate(hxs.xpath('//td[@class="titleBar"]')):
				try:				
					header=hxs.xpath("//td[@class='titleBar']")[i]	
					header=header.xpath('table[@width="100%"]/tr/td/b/text()').extract()	
					namen=header[0]
					name+=namen+dateSplitter
					daten=header[1]
					date+=daten+dateSplitter
				except:
					name+=dateSplitter
					date+=dateSplitter		
				try:				
					HWlinkn=hxs.xpath("//table[@class='table1']")[i]
					HWlinkn=HWlinkn.xpath('tr[2]/td/table/tr/td/li/a/@href').extract()	
					HWlink+=HWlinkn[0]+dateSplitter
				except:
					HWlink+=dateSplitter
		item['name']=name.replace('\r\n','').replace('\t','')
		item['Deadline']=date.replace('\r\n','').replace('\t','')
		item['HWlink']=HWlink.replace('\r\n','').replace('\t','')		
		yield item





