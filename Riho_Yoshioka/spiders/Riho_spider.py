import scrapy
from Riho_Yoshioka.items import RihoYoshiokaItem


class RihoSpider(scrapy.Spider):
    name = 'Riho'
    # download_delay = 0.5
    # allowed_domains = ['douban.com']
    start_urls = [
        "https://movie.douban.com/celebrity/1348382/photos/"
    ]

    def start_requests(self):
        yield scrapy.Request("https://movie.douban.com/celebrity/1348382/photos/", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"})

    def parse(self, response):
        for url in response.xpath("//ul/li/div/a/img/@src"):
            item = RihoYoshiokaItem()
            item["ImageAddress"] = url.extract()
            yield item

        next_page = response.css("div.paginator > span.next > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)
