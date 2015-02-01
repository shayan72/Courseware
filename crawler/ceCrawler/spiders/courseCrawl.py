import scrapy
import lxml.html
import re
import urllib2
from ceCrawler.items import course
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
    name = "courseCrawler"
    allowed_domains = ["http://ce.sharif.ir"]
    start_urls = first()
    def parse(self, response):
		hxs = Selector(response)
		item=course()
		item['link']=response.url
		try:
			item['name']=hxs.xpath("//td/span/text()")[0].extract()
		except:
			pass
		url=response.url
		try:		
			m=re.match(r'http://ce.sharif.edu/courses/(.*?)/ce*',url)
			item['term']=m.group(1)
			grp=hxs.xpath("//td[@class='semester']/text()").extract()

			#re.match(r'.*? Group (\d?) *',grp[0]).group(1)	
			item['group']=grp[0]
		except:
			pass

		try:				
			item['professors']=hxs.xpath('//tr/td/table/tr/td/a/b/text()')[0].extract()
		except:
			pass
		syll=url+"/index.php/section/syllabus/file/syllabus"
		item['teacher_assistants']=giveTAS(syll)
		item['picture']=url+"syllabus/Logo"
		
		
		yield item





