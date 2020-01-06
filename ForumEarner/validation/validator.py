import re

import unidecode


def valid_age(content):
    age = re.search(r'(\n|>).iek.*?(\d{2})', content)
    if age:
        age = age.group(2).replace('/strong>', '')

    return age


def valid_stack(content):
    stack = re.search(r'(\n|>)(.tanowisko|.echnologia|.echnologie|..zyk).(.*)<', content)
    if stack:
        stack = stack.group(3).replace('/strong>', '').replace('&gt;', '') \
            .replace('&lt', '').replace(':', '').strip()

    return stack


def valid_experience(content):
    exp = re.search(r'(\n|>)(.o.wiadczenie|.o.w).(.*)<', content)
    if exp:

        exp = exp.group(3).replace('/strong>', '').replace('&gt;', '') \
            .replace('&lt', '').replace(',', '.').replace(':', '').strip()

        if 'brak' in exp or 'staż' in exp or 'praktyki' in exp:
            exp = 0
        elif re.search(r'(msc|mies|mc|m-c|m-cy|miechy)', exp) is None:
            if re.search(r"rok\s", exp) or re.search(r'rok$', exp):
                exp = 1
            elif re.search(r'p...roku', exp):
                exp = 0.5
            elif re.search(r'(\d)-(\d)', exp):
                exp = re.search(r'(\d)-(\d)', exp).group(1)
            elif re.search(r'\d+.\d+', exp):
                exp = re.search(r'\d+.\d+', exp).group(0)
            elif re.search(r'\d+', exp):
                exp = re.search(r'\d+', exp).group(0)
            else:
                exp = 0
        else:
            if len(re.findall(r'[0-9]+', exp)) > 1:
                regex = re.search(r'(\d+).*?(\d+)', exp)
                exp = int(regex.group(1)) + int(regex.group(2))
                exp = round(float(exp / 12), 2)
            elif re.search(r'rok.*?(\d+)', exp):
                exp = float(1.0 + float(int(re.search(r'rok.*?(\d+)', exp).group(1))) / 12)
            elif re.search(r'rok.*', exp):
                exp = 1
            elif re.search(r'staż', exp):
                exp = 0
            else:
                exp = int(re.search(r'(\d+)', exp).group(1))
                exp = round(float(exp / 12), 2)
    # RETURN NONE IF BULLSHIT
    # {"exp": "2", "post-content": "\ndoświadczenie: ~10 lat, ale w różnych językach. c/c++ około 2-3 lat<"},
    # {"exp": "8", "post-content": "\ndoświadczenie: 8 lat, ale różne języki, na aktualnym stanowisku ~2 lata<"},
    # {"exp": 0.92,"post-content": "\ndoświadczenie: 3 miesiące zawodowo, wcześniej kilkanaście zleceń, programowaniem interesuję się od 8 lat<"},
    # {"exp": 1, "post-content": "\ndoświadczenie: 2,5 roku, piąty rok studiów<"},
    # {"exp": 1, "post-content": "\ndoświadczenie: 3 lata(granty, projekty naukowe) + 1 rok komercyjnego<"}
    # {"exp": 1.08, "post-content": "\ndoświadczenie: 6-7 miesięcy<"},
    # {"exp": 1.08, "post-content": "\ndoświadczenie: 2 lata 11 miesięcy (prawie 3 lata :))<"},
    # {"exp": 2.33,"post-content": "\ndoświadczenie: czysto komercyjne 10 miesięcy, wcześniej prowadzenie działalności przez 18 miesięcy i wytwarzanie oprogramowania dla januszów z różnym skutkiem<"},
    # {"exp": 0.5, "post-content": "\ndoświadczenie: 1,5 miesiąca<"},
    # {"exp": 1, "post-content": "\ndoświadczenie: 3,5 roku (1 rok automatyzacja)<"},
    # {"exp": "2", "post-content": "\ndoświadczenie: 2 lata jako student (na magisterskie przeniosłem się na informatykę), 0 komercyjnie<"},
    # if 'rok' na koniec dac bo psuje all
    # if komercyjne
    return exp


def valid_salary(content):
    salary = re.search(r'(\n|>)(.ynagrodzenie|.arobki|.tawka|.asa).(.*)<', content)
    if salary:
        salary = salary.group(3).replace('/strong>', '').replace('&gt;', '') \
            .replace('&lt', '').replace(':', '').strip()

        if 'uop' in content or 'umowa o prac' in content or 'etat' in content:
            salary = 1
        elif 'b2b' in content or 'vat' in content or 'fv' in content:
            salary = 2
        elif 'uz' in content or 'zlecenie' in content:
            salary = 3
        elif 'ud' in content or 'umowa o dzie' in content:
            salary = 4
        elif 'freelancer' in content:
            salary = 5
        else:
            # if 70k / per hour
            print('here ' + salary)
            print(content)

    return salary


def valid_location(content):
    location = re.search(r'(\n|>)(.iasto|.iejsce|.okalizacja).(.*)<', content)
    if location:

        location = unidecode.unidecode(location.group(3).replace('/strong>', '').replace('&gt;', '').replace('&lt', '')
                                       .replace(':', '').strip())

        if 'zdaln' in location or 'on-line' in location or 'google play' in location or 'remote' in location:
            location = 'zdalnie'
        elif 'wwa' in location or 'wawa' in location or 'stolica' in location or 'stolyca' in location or 'warszafka' in location:
            location = 'warszawa'
        elif 'krakow' in location or 'krk' in location:
            location = 'krakow'
        elif 'trojmiasto' in location or 'gdansk' in location or '3city' in location:
            location = 'gdansk'
        elif 'wroclaw' in location:
            location = 'wroclaw'

    return location
