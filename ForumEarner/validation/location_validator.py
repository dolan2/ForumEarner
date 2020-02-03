import re

import unidecode


def valid_location(content):
    location = re.search(r'(\n|>)(.iasto|.iejsce|.okalizacja).(.*)<', content)
    if location:

        location = unidecode.unidecode(location.group(3).replace('/strong>', '').replace('&gt;', '').replace('&lt', '')
                                       .replace(':', '').strip())

        if 'zdaln' in location or 'on-line' in location or 'google play' in location or 'remote' in location:
            location = 'zdalnie'
        elif 'warszawa' in location or 'wwa' in location or 'wawa' in location or 'stolica' in location \
                or 'stolyca' in location or 'warszafka' in location or 'w-wa' in location or 'waw' in location or 'sloikowo' in location:
            location = 'Warszawa'
        elif 'krakow' in location or 'krk' in location:
            location = 'Kraków'
        elif 'trojmiasto' in location or 'gdansk' in location or '3city' in location or '3miasto' in location:
            location = 'Trójmiasto Gdańsk'
        elif 'wroclaw' in location or 'wrocek' in location or 'woclaw' in location:
            location = 'Wrocław'
        elif 'poznan' in location:
            location = 'Poznań'
        elif 'lodz' in location:
            location = 'Łódź'
        elif 'rzeszow' in location:
            location = 'Rzeszów'
        elif 'torun' in location:
            location = 'Toruń'
        elif 'bialystok' in location:
            location = 'Białystok'
        elif 'katowice' in location:
            location = 'Śląsk Katowice'
        elif 'bydgoszcz' in location:
            location = 'Bydgoszcz'
        elif 'kielce' in location:
            location = 'Kielce'
        elif 'lublin' in location:
            location = 'Lublin'
        elif 'olsztyn' in location:
            location = 'Olsztyn'
        elif 'opole' in location:
            location = 'Opole'
        elif 'szczecin' in location:
            location = 'Szczecin'
        elif 'zielona gora' in location:
            location = 'Zielona Góra'
        elif 'gorzow' in location or 'gorzów' in location:
            location = 'Gorzów Wielkopolski'
        elif 'slask' in location:
            location = 'Śląsk'
        elif 'b-b' in location or 'bielsko' in location:
            location = 'Śląsk Bielsko-Biała'
        elif 'czestochowa' in location or 'częstochowa' in location:
            location = 'Śląsk Częstochowa'
        elif 'gliwice' in location:
            location = 'Śląsk Gliwice'
        elif 'sosnowiec' in location:
            location = 'Śląsk Sosnowiec'
        elif 'zabrze' in location:
            location = 'Śląsk Zabrze'
        elif 'bytom' in location:
            location = 'Śląsk Bytom'
        elif 'rybnik' in location:
            location = 'Śląsk Rybnik'
        elif 'tychy' in location:
            location = 'Śląsk Tychy'
        elif 'gdynia' in location:
            location = 'Trójmiasto Gdynia'
        elif 'sopot' in location:
            location = 'Trójmiasto Sopot'
        elif 'lomza' in location:
            location = "Other Łomża"
        elif 'chelm' in location:
            location = 'Other Chełm'
        elif 'nowy sacz' in location:
            location = 'Other Nowy Sącz'
        elif 'pn' in location:
            location = 'Poznań'
        else:
            location = 'Other ' + location

        if len(location.split()) > 10:
            location = None
        else:
            location = location.title()
            location = re.sub(r'\(.*?\)', '', location)

    return location
