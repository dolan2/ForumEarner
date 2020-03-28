import re


def valid_salary(content):
    salary = re.search(r'(\n|>)(.ynagrodzenie|.arobki|.tawka|.asa).(.*)<', content)
    if salary:
        salary = salary.group(3).replace('/strong>', '').replace('&gt;', '') \
            .replace('&lt', '').replace(':', '').replace(',', '.').strip()

        if re.search(r'.*?(^|\W)uop($|\W).*', content) or re.search(r'(^|\W)umowa o prac.($|\W)', content) \
                or re.search(r'(^|\W)etat($|\W)', content) and 'zlecenie' not in content:
            salary = get_salary(salary, 'UoP')
        elif re.search(r'(^|\W)b2b($|\W)', content) or re.search(r'.*vat($|\W)', content) or re.search(r'.*\Wfv($|\W)', content) \
                or re.search(r'(^|\W)działalno.*', content):
            salary = get_salary(salary, 'B2B')
        elif re.search(r'(^|\W)uz($|\W)', content) or re.search(r'(^|\W)zlecenie($|\W)', content):
            salary = get_salary(salary, 'UZ')
        elif re.search(r'(^|\W)ud($|\W)', content) or re.search(r'(^|\W)umowa o dzie.*', content) or re.search(
                r'(^|\W)uod\W.*', content):
            salary = get_salary(salary, 'UoD')
        elif 'freelancer' in content:
            salary = None
        elif re.search(r'(^|\W)kontrakt.*', content):
            salary = get_salary(salary, 'B2B')
        elif re.search(r'\d', salary) is not None:
            salary = get_salary(salary, 'None')
        else:
            salary = None

    return salary


def get_salary(salary, contract_type):
    global currency, taxes

    regex_comma_thousands_k = r'(.*?|^)(\d+)(\.|,)(\d+)(|\s)k.*'
    regex_comma_thousands_tys = r'(^|.*?)(\d+)(\.|,)(\d+).{0,5}(tyś|tys|tysiecy).*'
    regex_comma_hours = r'(^|.*?)(\d+)(\.|,)(\d+).{0,15}(/h|/ h|/g|/ g|godz|godzine|godzinę|rbh).*'
    regex_comma_days = r'(^|.*?)(\d+)(\.|,)(\d+).{0,15}(dzien|dziennie|dzień|per day|md|/d|/ d).*'
    regex_comma_others = r'(^|.*?)(\d+)(\.|,|\s|\')(\d+).*'

    regex_thousands_tys = r'(^|.*?)(\d+).{0,5}(tyś|tys|tysiecy).*'
    regex_hours = r'(^|.*?)(\d+).{0,15}(/h|/ h|/g|/ g|godz|godzine|godzinę|rbh).*'
    regex_days = r'(^|.*?)(\d+).{0,15}(dzien|dziennie|dzień|per day|md|/d|/ d).*'

    if re.search(r'(^|.*?)(\d+)(\.|,|\s|\')(\d+)(.*?|$)', salary):
        if re.search(regex_comma_hours, salary):
            first_part = re.search(regex_comma_hours, salary).group(2)
            second_part = re.search(regex_comma_hours, salary).group(4)
            contract_salary = int(first_part) * 160 + int(second_part) * 160 / 10
        elif re.search(regex_comma_days, salary):
            first_part = re.search(regex_comma_days, salary).group(2)
            second_part = re.search(regex_comma_days, salary).group(4)
            contract_salary = int(first_part) * 20 + int(second_part) * 10
        elif re.search(regex_comma_thousands_tys, salary):
            first_part = re.search(regex_comma_thousands_tys, salary).group(2)
            second_part = re.search(regex_comma_thousands_tys, salary).group(4)
            contract_salary = int(first_part) * 1000 + int(second_part) * 100
        elif re.search(regex_comma_thousands_k, salary):
            first_part = re.search(regex_comma_thousands_k, salary).group(2)
            second_part = int(re.search(regex_comma_thousands_k, salary).group(4))
            if second_part < 100:
                second_part *= 100
            contract_salary = int(first_part) * 1000 + second_part
        else:
            first_part = str(re.search(regex_comma_others, salary).group(2))
            second_part = str(re.search(regex_comma_others, salary).group(4))
            contract_salary = int(first_part + second_part)

            if contract_salary < 100:
                contract_salary *= 100
    else:
        if re.search(regex_hours, salary):
            contract_salary = int(re.search(regex_hours, salary).group(2)) * 160
        elif re.search(regex_days, salary):
            contract_salary = int(re.search(regex_days, salary).group(2)) * 20
        elif re.search(regex_thousands_tys, salary):
            contract_salary = int(re.search(regex_thousands_tys, salary).group(2)) * 1000
        elif re.search(r'(^|.*?)(\d+)(|\s)k(.*?|$)', salary):
            if re.search(r'(\s|^)(\d+).*?\dk.*', salary) is None:
                contract_salary = int(re.search(r'(^|.*?)(\d+)(|\s)k(.*?|$)', salary).group(2)) * 1000
            else:
                contract_salary = int(re.search(r'(^|.*?)(\d+)(.*?|$)', salary).group(2))
                if contract_salary < 100:
                    contract_salary *= 1000
        else:
            contract_salary = int(re.search(r'(^|.*?)(\d+)(.*?|$)', salary).group(2))

        if 'rok' in salary or 'roczna' in salary or 'rocznie' in salary:
            contract_salary /= 12

    if contract_salary is not None:

        contract_salary = int(contract_salary)

        if contract_salary < 25 and len(re.findall(r'[0-9]', salary)) < 3:
            contract_salary *= 1000

        if '€' in salary or 'eur' in salary:
            currency = 'eur'
        elif '$' in salary or 'usd' in salary:
            currency = 'usd'
        elif '£' in salary or 'gbp' in salary:
            currency = 'gbp'
        else:
            currency = 'pln'

        if 'brutto' in salary:
            taxes = 'Brutto'
            if 'b2b' in contract_type:
                taxes = 'Netto'
        elif 'netto' in salary or 'na rek' in salary:
            if 'uop' in contract_type:
                contract_salary = int(round(contract_salary * 1.33, -2))
                taxes = 'Brutto'
            else:
                taxes = 'Netto'
        else:
            if 'b2b' in contract_type:
                taxes = 'Netto'
            else:
                if 'uop' in contract_type and (contract_salary % 1000 == 0 or contract_salary > 7000):
                    taxes = 'Brutto'
                taxes = 'None'

        if contract_salary < 2000 or contract_salary > 80000:
            contract_salary = None

    return [contract_salary, currency, taxes, contract_type]
