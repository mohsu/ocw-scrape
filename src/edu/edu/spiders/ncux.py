import scrapy

url = "https://sites.google.com/view/ncuxocw/%E8%AA%B2%E7%A8%8B%E6%A8%A1%E7%B5%84"

class NcuxSpider(scrapy.Spider):
    name = 'NCUX'
    allowed_domains = ['google.com']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse_main)
    
    def parse_main(self, response):
        courses = response.xpath('//*[@id="h.p_9jltwX5-LizV"]')
        yield scrapy.Request(courses[0].xpath(".//a/@href").get(), callback=self.parse_course)
    
    def parse_course(self, response):
        # https://i-ocw.ctld.ncku.edu.tw/site/course_content/F22200_rh9c
        videos = response.xpath("//div[@class='video-name']")
        pass