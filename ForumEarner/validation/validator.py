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

        if re.search(r'(\d|rok.*|lat.*|mies.*)',
                     exp) is None and 'brak' not in exp and 'staż' not in exp and 'praktyk' not in exp and 'pierwsza praca' not in exp:
            exp = None
        elif 'brak' in exp or 'staż' in exp or 'praktyk' in exp or 'pierwsza praca' in exp and re.search(r'\d',
                                                                                                         exp) is None:
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
            .replace('&lt', '').replace(':', '').replace(',', '.').strip()

        if re.search(r'.*?uop.*?', content) or re.search(r'.*?umowa o prac.*?', content) or re.search(r'.*?etat.*?', content):
            salary = get_salary(salary, 'uop')
        elif re.search(r'.*?b2b.*?', content) or re.search(r'.*?vat.*?', content) or re.search(r'.*?fv.*?', content) or re.search(r'.*?kontrakt.*?', content) or re.search(r'.*?działalno.*?', content):
            salary = get_salary(salary, 'b2b')
        elif re.search(r'.*?uz.*?', content) or re.search(r'.*?zlecenie.*?', content):
            salary = get_salary(salary, 'uz')
        elif re.search(r'.*?ud.*?', content) or re.search(r'.*?umowa o dzie.*?', content) or re.search(r'.*?uod.*?', content):
            salary = get_salary(salary, 'uod')
        elif 'freelancer' in content:
            salary = None
        elif re.search(r'\d', salary) is not None:
            salary = get_salary(salary, 'brak3')
        else:
            salary = None

    return salary


def get_salary(salary, contract_type):

    if re.search(r'.*?(\d+)(\.|,|\s|\')(\d+).*?', salary):
        if re.search(r'.*?(\d+)(\.|,)(\d+)(|\s)k.*?', salary):
            first_part = re.search(r'.*?(\d+)(\.|,)(\d+)(|\s)k.*?', salary).group(1)
            second_part = re.search(r'.*?(\d+)(\.|,)(\d+)(|\s)k.*?', salary).group(3)
            contract_salary = int(first_part) * 1000 + int(second_part) * 100
        elif re.search(r'.*?(\d+)(\.|,)(\d+).*?(tyś|tys).*?', salary):
            first_part = re.search(r'.*?(\d+)(\.|,)(\d+).*?(tyś|tys).*?', salary).group(1)
            second_part = re.search(r'.*?(\d+)(\.|,)(\d+).*?(tyś|tys).*?', salary).group(3)
            contract_salary = int(first_part) * 1000 + int(second_part) * 100
        elif re.search(r'.*?(\d+)(\.|,)(\d+).*?(/h|/ h|/g|/ g|godz.*|rbh).*?', salary):
            first_part = re.search(r'.*?(\d+)(\.|,)(\d+).*?(/h|/ h|/g|/ g|godz.*|rbh).*?', salary).group(1)
            second_part = re.search(r'.*?(\d+)(\.|,)(\d+).*?(/h|/ h|/g|/ g|godz.*|rbh).*?', salary).group(3)
            contract_salary = int(first_part) * 160 + int(second_part)/10 * 100
        elif re.search(r'.*?(\d+)(\.|,)(\d+).*?(dzien.*|dzień|per day|md|/d|/ d).*?', salary):
            first_part = re.search(r'.*?(\d+)(\.|,)(\d+).*?(dzien.*|dzień|per day|md|/d|/ d).*?', salary).group(1)
            second_part = re.search(r'.*?(\d+)(\.|,)(\d+).*?(dzien.*|dzień|per day|md|/d|/ d).*?', salary).group(3)
            contract_salary = int(first_part) * 20 + int(second_part) * 10
        else:
            first_part = str(re.search(r'.*?(\d+)(\.|,|\s|\')(\d+).*?', salary).group(1))
            second_part = str(re.search(r'.*?(\d+)(\.|,|\s|\')(\d+).*?', salary).group(3))
            contract_salary = int(first_part + second_part)

            if contract_salary < 100:
                contract_salary *= 100
    else:
        if re.search(r'.*?(\d+)(|\s)k.*?', salary):
            contract_salary = int(re.search(r'.*?(\d+)(|\s)k.*?', salary).group(1)) * 1000
        elif re.search(r'.*?(\d+).*?(tyś|tys.*).*?', salary):
            contract_salary = int(re.search(r'.*?(\d+).*?(tyś|tys.*).*?', salary).group(1)) * 1000
        elif re.search(r'.*?(\d+).*?(/h|/ h|/g|/ g|godz.*|rbh).*?', salary):
            contract_salary = int(re.search(r'.*?(\d+).*?(/h|/ h|/g|/ g|godz.*|rbh).*?', salary).group(1)) * 160
        elif re.search(r'.*?(\d+).*?(dzien.*|dzień|per day|md|/d|/ d).*?', salary):
            contract_salary = int(re.search(r'.*?(\d+).*?(dzien.*|dzień|per day|md|/d|/ d).*?', salary).group(1)) * 20
        else:
            contract_salary = int(re.search(r'.*?(\d+).*', salary).group(1))

    if contract_salary is not None:

        if contract_salary < 15 and len(re.findall(r'[0-9]', salary)) < 3:
            contract_salary *= 1000

        if '€' in salary or 'eur' in salary:
            contract_salary = str(contract_salary) + ' eur'
        elif '$' in salary or 'usd' in salary:
            contract_salary = str(contract_salary) + ' usd'
        elif '£' in salary or 'gbp' in salary:
            contract_salary = str(contract_salary) + ' gbp'
        else:
            contract_salary = str(contract_salary) + ' pln'

        if 'brutto' in salary:
            contract_salary += ' brutto ' + contract_type
        elif 'netto' in salary or 'na rek' in salary:
            contract_salary += ' netto ' + contract_type
        else:
            contract_salary += ' brak2 ' + contract_type

        if re.search(r'.*?(\d+).*?', contract_salary):
            temp_salary = int(re.search(r'.*?(\d+).*?', contract_salary).group(1))
            if temp_salary > 50000 or temp_salary < 500:
                contract_salary = None

    return contract_salary


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
