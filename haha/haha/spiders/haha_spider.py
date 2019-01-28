import scrapy

class MohaSpider(scrapy.Spider):
	name = "moha"
	def start_requests(self):
		urls=['https://en.wikipedia.org/wiki/Jiang_Zemin']
		for url in urls:
			yield scrapy.Request(url=url,callback = self.parse)
	def parse(self,response):
		page = response.url.split("/")[-2]
		filename =  'quotes-%s.html' % page
		with open('test.txt','wb') as f:
			f.write(response.body)
		self.log("Save")
