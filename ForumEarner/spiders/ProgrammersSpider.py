import scrapy


class ProgrammersSpider(scrapy.Spider):
    name = "4p"

    def start_requests(self):
        url = 'https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.css('div.post'):
            yield {
                'date': post.css('span.timestamp::text').get(),
                'post-content': post.css('div.post-content').get()
            }

        next_page = response.css('ul.pagination').css('li')[-1].css('a::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(url='https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie/' + next_page)