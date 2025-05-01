
import flist
import re
from .Character import Character
from bs4 import BeautifulSoup


def _get_side_info(soup, box:str):
    statbox = soup.find('div', {'class', box})

    raw_text = str((statbox))
    raw_text = raw_text.replace('\n', '').replace('\r', '').replace('\t', ' ').replace('<br/>', '\n')

    regex = '<span class="taglabel">([a-zA-Z0-9 \/]+)<\/span>:[ ]+([a-zA-Z0-9 \/,._-]+)'
    pattern = re.compile(regex)

    return re.findall(pattern, raw_text)


def _get_tab_info(soup, box:str):
    statbox = soup.find('div', {'class', box})

    raw_text = str((statbox))
    raw_text = raw_text.replace('\n', '').replace('\r', '').replace('\t', ' ').replace('<br/>', '\n')

    regex = '<span class="taglabel">([a-zA-Z0-9 \/]+):<\/span>[ ]*([a-zA-Z0-9 \/,._-]+)'
    pattern = re.compile(regex)

    return re.findall(pattern, raw_text)


def _get_kinks(soup, box:str):
    pass


def get_character(character_name:str):
    if not character_name:
        return None
    
    url = f'https://www.f-list.net/c/{character_name}'

    session = flist.session()
    request = session.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')
    try:
        charname = soup.find('span', {'class', 'charname'}).text

        found = _get_side_info(soup, 'statbox')

        character = Character(charname)

        for key, value in found:
            _key = key.lower().replace(' ', '_')
            character.set_attribute(_key, value)
        
        character.set_attribute("id", request.cookies["account_default_character_id"])

        found = _get_tab_info(soup, 'infodatabox')
        for key, value in found:
            _key = key.lower().replace(' ', '_')
            character.set_attribute(_key, value)

        return character

    # todo: kinks

    except Exception as e:
        print(f"Exception: {e}")
        return None

