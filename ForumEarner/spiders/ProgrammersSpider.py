from datetime import datetime
import scrapy
import re

# posts on 247 pages:
# 2964 all with None (11 posts + 1 post always null)
# 2717 <div> if date is not None (11 posts per page)
# 2470 <div> if remove title post on each page(10 posts per page)
# 2105 <div> contains 'wiek' or 'Wiek'
# wiek 2743
# stanowisko 2361, technologia 391, technologie 479, jezyk 42
# doświadczenie 2656, doswiadczenie 65
# zarobki 2341, wynagrodzenie 79 kasa 22
# miasto 2385, miejsce 155
# 1534 <div> contains all above
# 1559 <p> with all above

# Check if this working lol
class ProgrammersSpider(scrapy.Spider):
    name = "4p"

    def start_requests(self):
        url = 'https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for div_post in response.css('div.post'):
            date = str(div_post.css('span.timestamp::text').get()).split()[0]

            if date is not None and date != '2014-05-05':
                if 'dziś' in date:
                    date = datetime.date(datetime.now())

                age = 'wiek'
                position = ['stanowisko', 'technologia', 'technologie', 'jezyk']
                experience = ['doświadczenie', 'doswiadczenie']
                salary = ['zarobki', 'wynagrodzenie', 'kasa']
                place = ['miasto', 'miejsce', 'lokalizacja']

                div_post_content = str(div_post.css('div.post-content').get()).lower()
                if age in div_post_content \
                        and any(ele in div_post_content for ele in position) \
                        and any(ele in div_post_content for ele in experience) \
                        and any(ele in div_post_content for ele in salary) \
                        and any(ele in div_post_content for ele in position) \
                        and any(ele in div_post_content for ele in place):

                    content = ''
                    for p_tag in div_post.css('div.post-content p'):
                        if age in str(p_tag.get()).lower():
                            content = p_tag.get()

                    if content != '':
                        yield {
                            'date': date,
                            'post-content': content
                        }

        next_page = response.css('ul.pagination').css('li')[-1].css('a::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(url='https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie/' + next_page)
