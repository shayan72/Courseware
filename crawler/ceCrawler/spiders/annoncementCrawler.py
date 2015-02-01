import scrapy
import lxml.html
import re
import urllib2
from ceCrawler.items import announcments
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
            list.append( json.loads(line)['link'])
    return list



def giveTAS(syll):
    html = lxml.html.parse(syll)
    xp1='//table/tr[4]/td/table/tr/td/ul/li/a[1]/text()'
    first=filter(lambda x:not '@' in x ,html.xpath(xp1))
    xp2='//table/tr[4]/td/table/tr/td/ul/li/text()'
    second= filter(lambda x: x!='',map(lambda x:x.split(',')[0] ,html.xpath(xp2)))
    return first+second

class DmozSpider(scrapy.Spider):
    name = "announcmentsCrawler"
    allowed_domains = ["http://ce.sharif.ir"]
    start_urls = first()
    def parse(self, response):
		hxs = Selector(response)
		item=announcments()
		item['link']=response.url
		titem=[]
		dateSplitter="||||||||||" #10 ta \
		anonsSplitter="**********" #10 ta *
		this=""		
		for i,x in enumerate(hxs.xpath('//table[@class="titlebar"]')):
								
				date=hxs.xpath("//table[@class='titlebar']")[i]			
				date=date.xpath('tbody/tr[1]/td[@align="right"]/text()').extract()
				date=date[0]
				this+=date+dateSplitter
				table1=hxs.xpath("//table[@class='table1']/tr/td/table/tr")[i]
				context=table1.xpath('td/text()').extract()
				context=''.join(context)				
				this+=context+anonsSplitter
				this=this.replace('\t','').replace('\r\n','')
		item['annons']=this
		
		
		yield item





