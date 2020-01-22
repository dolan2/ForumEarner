import re


def valid_salary(content):
    salary = re.search(r'(\n|>)(.ynagrodzenie|.arobki|.tawka|.asa).(.*)<', content)
    if salary:
        salary = salary.group(3).replace('/strong>', '').replace('&gt;', '') \
            .replace('&lt', '').replace(':', '').replace(',', '.').strip()

        if re.search(r'.*?\Wuop\W.*?', content) or re.search(r'.*?\Wumowa o prac.\W.*?', content) \
                or re.search(r'.*?\Wetat\W.*?', content) and 'zlecenie' not in content:
            salary = get_salary(salary, 'uop')
        elif re.search(r'.*?b2b.*?', content) or re.search(r'.*?vat.*?', content) or re.search(r'.*?\Wfv.*?', content) \
                or re.search(r'.*?kontrakt.*?', content) or re.search(r'.*?działalno.*?',
                                                                      content) and 'umowa o dzie' not in content:
            salary = get_salary(salary, 'b2b')
        elif re.search(r'.*?\Wuz\W.*?', content) or re.search(r'.*?zlecenie.*?', content):
            salary = get_salary(salary, 'uz')
        elif re.search(r'.*?\Wud\W.*?', content) or re.search(r'.*?umowa o dzie.*?', content) or re.search(
                r'.*?\Wuod\W.*?', content):
            salary = get_salary(salary, 'uod')
        elif 'freelancer' in content:
            salary = None
        elif re.search(r'\d', salary) is not None:
            salary = get_salary(salary, '?')
        else:
            salary = None

    return salary


def get_salary(salary, contract_type):
    global currency, taxes
    if re.search(r'(.*?|^)(\d+)(\.|,|\s|\')(\d+).*?', salary):
        if re.search(r'(.*?|^)(\d+)(\.|,)(\d+)(|\s)k.*?', salary):
            first_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+)(|\s)k.*?', salary).group(2)
            second_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+)(|\s)k.*?', salary).group(4)
            contract_salary = int(first_part) * 1000 + int(second_part) * 100
        elif re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(tyś|tys|tysiecy).*?', salary):
            first_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(tyś|tys|tysiecy).*?', salary).group(2)
            second_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(tyś|tys|tysiecy).*?', salary).group(4)
            contract_salary = int(first_part) * 1000 + int(second_part) * 100
        elif re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(/h|/ h|/g|/ g|godz|godzine|rbh).*?', salary):
            first_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(/h|/ h|/g|/ g|godz|godzine|rbh).*?', salary).group(2)
            second_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(/h|/ h|/g|/ g|godz|godzine|rbh).*?', salary).group(4)
            contract_salary = int(first_part) * 160 + int(second_part) / 10 * 100
        elif re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(dzien|dziennie|dzień|per day|md|/d|/ d).*?', salary):
            first_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(dzien|dziennie|dzień|per day|md|/d|/ d).*?', salary).group(2)
            second_part = re.search(r'(.*?|^)(\d+)(\.|,)(\d+).{1,5}(dzien|dziennie|dzień|per day|md|/d|/ d).*?', salary).group(4)
            contract_salary = int(first_part) * 20 + int(second_part) * 10
        else:
            first_part = str(re.search(r'(.*?|^)(\d+)(\.|,|\s|\')(\d+).*?', salary).group(2))
            second_part = str(re.search(r'(.*?|^)(\d+)(\.|,|\s|\')(\d+).*?', salary).group(4))
            contract_salary = int(first_part + second_part)

            if contract_salary < 100:
                contract_salary *= 100
    else:
        if len(re.findall(r'(\s|^)(\d+)', salary)) < 2 and re.search(r'(\s|^)(\d+).*?\dk.*', salary) is None:
            if re.search(r'(.*?|^)(\d+).{0,2}k.*?', salary):
                if 'rok' in salary or 'rocznie' in salary:
                    contract_salary = int(re.search(r'(.*?|^)(\d+).{0,2}k.*?', salary).group(2)) * 1000
                    contract_salary /= 12
                else:
                    contract_salary = int(re.search(r'(.*?|^)(\d+).{0,2}k.*?', salary).group(2)) * 1000
            elif re.search(r'(.*?|^)(\d+).{1,5}(tyś|tys|tysiecy).*?', salary):
                contract_salary = int(re.search(r'(.*?|^)(\d+).{1,5}(tyś|tys|tysiecy).*?', salary).group(2)) * 1000
            elif re.search(r'(.*?|^)(\d+).{1,5}(/h|/ h|/g|/ g|godz|godzine|rbh).*?', salary):
                contract_salary = int(re.search(r'(.*?|^)(\d+).{1,5}(/h|/ h|/g|/ g|godz|godzine|rbh).*?', salary).group(2)) * 160
            elif re.search(r'(.*?|^)(\d+).{1,5}(dzien|dziennie|dzień|per day|md|/d|/ d).*?', salary):
                contract_salary = int(re.search(r'(.*?|^)(\d+).{1,5}(dzien|dziennie|dzień|per day|md|/d|/ d).*?', salary).group(2)) * 20
            else:
                contract_salary = int(re.search(r'(.*?|^)(\d+).*', salary).group(2))

            if contract_salary > 80000 or contract_salary < 800:
                contract_salary = None
        else:
            print('hej ' + salary)
            contract_salary = int(re.search(r'(.*?|^)(\d+).*?', salary).group(2))

    if contract_salary is not None:

        if contract_salary < 15 and len(re.findall(r'[0-9]', salary)) < 3:
            contract_salary *= 1000

        contract_salary = int(contract_salary)

        if '€' in salary or 'eur' in salary:
            currency = 'eur'
        elif '$' in salary or 'usd' in salary:
            currency = 'usd'
        elif '£' in salary or 'gbp' in salary:
            currency = 'gbp'
        else:
            currency = 'pln'

        if 'brutto' in salary:
            taxes = 'brutto'
        elif 'netto' in salary or 'na rek' in salary:
            taxes = 'netto'
        else:
            if 'b2b' in contract_type:
                taxes = 'netto'
            else:
                if 'uop' in contract_type and (contract_salary % 1000 == 0 or contract_salary > 8000):
                    taxes = 'brutto'
                taxes = '!'

    return [contract_salary, currency, taxes, contract_type]
