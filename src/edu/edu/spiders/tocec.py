import scrapy

url = "https://www.tocec.org.tw/web/subjects_results.jsp"

class TocecSpider(scrapy.Spider):
    name = 'tocec'
    allowed_domains = ['tocec.org.tw']

    def start_requests(self):
        yield scrapy.Request(url=url, callback=self.parse_main)
    
    def parse_main(self, response):
        # table
        for tr in response.xpath("//tbody//tr"):
            school = tr.xpath(".//td[1]/text()").extract_first().strip()
            title = tr.xpath(".//td[2]/a/text()").extract_first()
            link = tr.xpath(".//td[2]/a/@href").extract_first()
            instructor = tr.xpath(".//td[3]/text()").extract_first()
            # yield scrapy.Request(response.urljoin(link), callback=self.parse_course)
        
        # next page
        if response.xpath("//li/a[@aria-label='Next']/@onclick"):
            next_page = response.xpath("//li[@class='page-item active']/following-sibling::li/a/text()").extract_first()
            yield scrapy.FormRequest.from_response(response=response, formid="form", formdata={"page_num": next_page}, callback=self.parse_main)
    
    def parse_course(self, response):
        object_ = response.xpath("//h3[contains(text(), '課程目標')]/text()").extract_first()
        course_url = response.xpath("//a[contains(text(), 'View Course')]")