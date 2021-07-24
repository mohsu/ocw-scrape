import scrapy


class OpeneduSpider(scrapy.Spider):
    name = 'openedu'
    allowed_domains = ['openedu.com.tw']

    def start_requests(self):
        curl = """curl 'https://www.openedu.tw/api/courses/search?lang=en' \
  -H 'authority: www.openedu.tw' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.openedu.tw/list.jsp' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: JSESSIONID=E63DDA521B1D3D5333C75C954E6AD344; _ga=GA1.2.1862219852.1627114671; _gid=GA1.2.963448872.1627114671; _gat=1' \
  --compressed"""
        yield scrapy.Request.from_curl(curl, callback=self.parse_main)
    
    def parse_main(self, response):
        # get json from main page
        
        # for id in courses
        # yield request f"https://www.openedu.tw/api/courses/{id}/lang/zh"
        pass
    
    def parse_course(self, response):
        # parse json
        pass