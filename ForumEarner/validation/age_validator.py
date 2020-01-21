import re


def valid_age(content):
    age = re.search(r'(\n|>).iek.*?(\d{2})', content)
    if age:
        age = age.group(2).replace('/strong>', '')

    if age is not None:
        if int(age) < 18:
            age = None

    return age
