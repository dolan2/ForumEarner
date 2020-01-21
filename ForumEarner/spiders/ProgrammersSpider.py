from datetime import datetime
import re
import scrapy

from ForumEarner.validation import age_validator
from ForumEarner.validation import experience_validator
from ForumEarner.validation import location_validator
from ForumEarner.validation import salary_validator
from ForumEarner.validation import stack_validator


class ProgrammersSpider(scrapy.Spider):
    name = "4p"

    def start_requests(self):
        url = 'https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for div_post in response.css('div.post'):
            date = str(div_post.css('span.timestamp::text').get()).split()[0]

            if date is not None and date != '2014-05-05':
                if 'dziś' in date or 'wczoraj' in date:
                    date = datetime.date(datetime.now())

                age = 'wiek'
                stack = ['stanowisko', 'technologia', 'technologie', 'jezyk']
                experience = ['doświadczenie', 'doswiadczenie', 'dosw']
                salary = ['zarobki', 'wynagrodzenie', 'stawka', 'kasa']
                place = ['miasto', 'miejsce', 'lokalizacja']

                div_post_content = str(div_post.css('div.post-content').get()).lower()
                if re.search(r'\|', div_post_content) is None and age in div_post_content \
                        and any(ele in div_post_content for ele in stack) \
                        and any(ele in div_post_content for ele in experience) \
                        and any(ele in div_post_content for ele in salary) \
                        and any(ele in div_post_content for ele in place):
                    content = ''
                    for p_tag in div_post.css('div.post-content > p'):
                        p_tag = str(p_tag.get()).lower()
                        if age in p_tag \
                                and any(ele in p_tag for ele in stack) \
                                and any(ele in p_tag for ele in experience) \
                                and any(ele in p_tag for ele in salary) \
                                and any(ele in p_tag for ele in place):
                            content = p_tag

                    if content != '':
                        content = content.lower()

                        age = age_validator.valid_age(content)
                        stack = stack_validator.valid_stack(content)
                        exp = experience_validator.valid_experience(content)
                        salary = salary_validator.valid_salary(content)
                        location = location_validator.valid_location(content)

                        if age is not None and stack is not None and exp is not None \
                                and salary is not None and None not in salary and location is not None:
                            yield {
                                'date': date,
                                'age': age,
                                'stack': stack,
                                'exp': exp,
                                'salary': salary[0],
                                'currency': salary[1],
                                'taxes': salary[2],
                                'contract_type': salary[3],
                                'location': location,
                                # 'post-content': content
                            }

        next_page = response.css('ul.pagination').css('li')[-1].css('a::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(url='https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie/' + next_page)
