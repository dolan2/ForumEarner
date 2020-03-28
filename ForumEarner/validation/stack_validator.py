import re


def valid_stack(content):
    stack = re.search(r'(\n|>)(.tanowisko|.echnologia|.echnologie|..zyk).(.*)<', content)
    if stack:
        stack = stack.group(3).replace('/strong>', '').replace('&gt;', '') \
            .replace('&lt', '').replace(':', '').strip()

    if 'javascript' in stack:
        stack = 'Javascript'
    elif 'java' in stack:
        stack = 'Java'
    elif 'c#' in stack:
        stack = '.NET'
    elif 'c++' in stack:
        stack = 'C++'
    elif 'php' in stack or 'magento' in stack or 'laravel' in stack or 'symfony' in stack:
        stack = 'PHP'
    elif 'python' in stack:
        stack = 'Python'
    elif 'ruby' in stack:
        stack = 'Ruby'
    elif 'kotlin' in stack:
        stack = 'Kotlin'
    elif 'swift' in stack:
        stack = 'iOS'
    elif 'golang' in stack:
        stack = 'Golang'
    elif 'rust' in stack:
        stack = 'Rust'
    elif 'vba' in stack:
        stack = 'Visual Basic'
    elif '.net' in stack:
        stack = '.NET'
    elif 'kernel' in stack:
        stack = 'Admin'
    elif 'android' in stack:
        stack = 'Android'
    elif 'ios' in stack:
        stack = 'iOS'
    elif 'ror' in stack:
        stack = 'Ruby'
    elif 'Embedded' in stack:
        stack = 'C'
    elif 'cobol' in stack:
        stack = 'Cobol'
    elif 'scala' in stack:
        stack = 'Scala'
    elif 'angular' in stack:
        stack = 'Javascript'
    elif 'react' in stack:
        stack = 'Javascript'
    elif 'web' in stack:
        stack = 'Javascript'
    elif 'nodejs' in stack or 'node.js' in stack or 'node' in stack:
        stack = 'Javascript'
    elif 'django' in stack:
        stack = 'Python'
    elif 'front' in stack:
        stack = 'Javascript'
    elif 'anal' in stack:
        stack = 'Analityk'
    elif 'manual' in stack:
        stack = 'Testing'
    elif 'automat' in stack:
        stack = 'Testing'
    elif 'tester' in stack:
        stack = 'Testing'
    elif 'qa' in stack:
        stack = 'Testing'
    elif 'devops' in stack:
        stack = 'DevOps'
    elif 'admin' in stack:
        stack = 'Admin'
    elif 'sharepoint' in stack:
        stack = 'Developer'
    elif 'archite' in stack:
        stack = 'Architekt'
    elif 'js' in stack:
        stack = 'Javascript'
    elif '. net' in stack:
        stack = '.NET'
    elif 'test' in stack:
        stack = 'Testing'
    elif 'typescript' in stack:
        stack = 'Javascript'
    elif 'spring' in stack:
        stack = 'Java'
    elif 'bi' in stack or 'intelligence' in stack or 'konsultant' in stack or 'consultant' in stack or 'sas' in stack or 'erp' in stack:
        stack = 'Analityk'
    elif 'data' in stack or 'etl' in stack or 'dwh' in stack:
        stack = 'Analityk'
    elif 'system' in stack:
        stack = 'C'
    elif 'machine' in stack:
        stack = 'Python'
    elif 'wordpress' in stack:
        stack = 'Developer'
    elif 'support' in stack or 'help' in stack:
        stack = 'Helpdesk'
    elif 'delphi' in stack:
        stack = 'Delphi'
    elif 'net' in stack:
        stack = '.NET'
    elif 'sql' in stack:
        stack = 'SQL'
    elif 'salesforce' in stack:
        stack = 'Developer'
    elif 'lider' in stack or 'lead' in stack:
        stack = 'Team Leader'
    elif 'owner' in stack:
        stack = 'Product Owner'
    elif 'informatyk' in stack:
        stack = 'Informatyk'
    elif 'ux designer' in stack:
        stack = 'UX Designer'
    elif re.search(r'\sc$', stack) is not None or re.search(r'\sc\s', stack) is not None or re.search(r'^c$', stack) is not None:
        stack = 'C'
    elif 'developer' in stack or 'software' in stack or 'programista' in stack or 'dev' in stack or 'senior' in stack \
            or 'junior' in stack or 'stażysta' in stack or 'intern' in stack or 'backend' in stack or 'full' in stack:
        stack = 'Developer'
    else:
        stack = None

    if stack is not None:
        if stack is not 'iOS' and stack is not '.NET' and stack is not 'PHP' and stack is not 'SQL':
            stack = stack.title()

        stack = re.sub(r'\(.*?\)', '', stack)
        stack = stack[:40]

    return stack
