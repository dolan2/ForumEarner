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
            location = 'Gdańsk'
        elif 'wroclaw' in location or 'wrocek' in location or 'woclaw' in location:
            location = 'Wrocław'
        elif 'poznan' in location:
            location = 'Poznań'
        elif 'lodz' in location:
            location = 'Łódź'
        elif 'rzeszow' in location:
            location = 'Rzeszów'
        elif 'slask' in location:
            location = 'Śląsk'
        elif 'katowice' in location:
            location = 'Katowice'
        elif 'torun' in location:
            location = 'Toruń'
        elif 'b-b' in location or 'bielsko' in location:
            location = 'Bielsko-Biała'
        elif 'bialystok' in location:
            location = 'Białystok'
        elif 'pn' in location:
            location = 'Poznań'
        elif 'zielona gora' in location:
            location = 'Zielona Góra'
        elif 'czestochowa' in location:
            location = 'Częstochowa'
        elif 'lomza' in location:
            location = "Łomża"
        elif 'chelm' in location:
            location = 'Chełm'
        elif 'nowy sacz' in location:
            location = 'Nowy Sącz'
        elif 'gliwice' in location:
            location = 'Gliwice'

        if len(location.split()) > 10:
            location = None
        else:
            location = location.title()
            location = re.sub(r'\(.*?\)', '', location)

    return location
