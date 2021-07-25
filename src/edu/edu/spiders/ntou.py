import json
import scrapy


url = "https://www.o-channel.org/ocw"


class NtouSpider(scrapy.Spider):
    name = 'NTOU'
    allowed_domains = ['o-channel.org']

    def start_requests(self):
        # yield SeleniumRequest(url=url, callback=self.parse_main, 
        #                       wait_time=10, wait_until=EC.visibility_of_element_located((By.XPATH, "//div[@data-hook='info-element']")))
        yield scrapy.Request(url=url, callback=self.parse_main)

    def parse_main(self, response):
        text = response.xpath("//script[@id='wix-viewer-model']/text()").get()
        dic = json.loads(text)
        dic["siteFeaturesConfigs"][]
        yield scrapy.Request(courses[0].xpath(".//a/@href").get(), callback=self.parse_course)

    def parse_course(self, response):
        # https://i-ocw.ctld.ncku.edu.tw/site/course_content/F22200_rh9c
        videos = response.xpath("//div[@class='video-name']")
        pass
