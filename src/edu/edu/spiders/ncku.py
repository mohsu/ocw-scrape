import scrapy

url = "https://i-ocw.ctld.ncku.edu.tw/"

class NtuSpider(scrapy.Spider):
    name = 'NTU'
    allowed_domains = ['i-ocw.ctld.ncku.edu.tw']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse_main)
    
    def parse_main(self, response):
        courses = response.xpath("//div[@class='course-wrapper']")
        yield scrapy.Request(courses[0].xpath(".//a/@href").get(), callback=self.parse_course)
    
    def parse_course(self, response):
        # https://i-ocw.ctld.ncku.edu.tw/site/course_content/F22200_rh9c
        videos = response.xpath("//div[@class='video-name']")
        pass