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

        if re.search(r'(\d|rok.*|lat.*|mies.*)', exp) is None and 'brak' not in exp and 'staż' not in exp and 'praktyk' not in exp and 'pierwsza praca' not in exp:
            exp = None
        elif 'brak' in exp or 'staż' in exp or 'praktyk' in exp or 'pierwsza praca' in exp and re.search(r'\d', exp) is None:
            exp = 0
        elif re.search(r'(msc|mies|mc|m-c|m-cy|miechy|\dm|ms)', exp) is None:
            if re.search(r'(\d+)(-|/)(\d+)', exp) and len(re.findall(r'[0-9]+', exp)) <= 2:
                exp = re.search(r'(\d+)(-|/)(\d+)', exp).group(1)
            elif re.search(r'\d+.\d+', exp) and len(re.findall(r'[0-9]+', exp)) <= 2:
                exp = re.search(r'\d+.\d+', exp).group(0)
            elif re.search(r'\d+', exp):
                exp = re.search(r'\d+', exp).group(0)
            elif re.search(r"rok\s", exp) or re.search(r'rok$', exp):
                exp = 1
            elif re.search(r'p...roku', exp):
                exp = 0.5
            elif re.search(r'p..tora roku', exp):
                exp = 1.5
            else:
                exp = None
        elif re.search(r'(msc|mies|mc|m-c|m-cy|miechy|\dm|ms)', exp) is not None:
            if len(re.findall(r'[0-9]+', exp)) > 1:
                if re.search(r'(\d+).*?(lat|lat.|rok|rok.).*?(\d+)', exp) is not None:
                    regex = re.search(r'(\d+).*?(lat|lat.|rok|rok.).*?(\d+)', exp)
                    exp = round(float(regex.group(1)) + float(regex.group(3)) / 12, 2)
                elif re.search(r'(msc|mies|mc|m-c|m-cy|miechy|\dm|ms)', exp) is None:
                    exp = re.search(r'(\d+)', exp).group(1)
                else:
                    exp = round(float(re.search(r'(\d+)', exp).group(1)) / 12, 2)
            elif re.search(r'rok.*?(\d+)', exp):
                exp = round(float(1.0 + float(int(re.search(r'rok.*?(\d+)', exp).group(1))) / 12), 2)
            elif re.search(r'rok.*', exp):
                exp = 1
            elif re.search(r'(msc|mies|mc|m-c|m-cy|miechy|\dm|ms)', exp) is not None:
                exp = int(re.search(r'(\d+)', exp).group(1))
                exp = round(float(exp / 12), 2)
            else:
                exp = None
        else:
            exp = None

    if exp is not None:
        exp = float(exp)

    return exp


def valid_salary(content):
    salary = re.search(r'(\n|>)(.ynagrodzenie|.arobki|.tawka|.asa).(.*)<', content)
    if salary:
        salary = salary.group(3).replace('/strong>', '').replace('&gt;', '') \
            .replace('&lt', '').replace(':', '').strip()

        if 'uop' in content or 'umowa o prac' in content or 'etat' in content:
            salary = 1
        elif 'b2b' in content or 'vat' in content or 'fv' in content or 'kontrakt' in content:
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
