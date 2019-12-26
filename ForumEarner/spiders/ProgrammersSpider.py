import scrapy


class ProgrammersSpider(scrapy.Spider):
    name = "4p"

    def start_requests(self):
        url = 'https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pages = response.css('.pagination').css('a::text')[-2].extract()

        for pageNumber in range(0, pages):
            'https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie?page=' + str(pageNumber)
