import scrapy

url = "http://ocw.aca.ntu.edu.tw/ntu-ocw/ocw/coupage/1"

class NtuSpider(scrapy.Spider):
    name = 'NTU'
    allowed_domains = ['ocw.aca.ntu.edu.tw']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse_main)
    
    def parse_main(self, response):
        courses = response.xpath("//div[@class='coursebox']")
    
    def parse_course(self, response):
        # http://ocw.aca.ntu.edu.tw/ntu-ocw/ocw/cou/099S101
        pass