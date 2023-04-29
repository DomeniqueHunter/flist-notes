
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


def get_character(character_name:str):
    url = f'https://www.f-list.net/c/{character_name}'
    
    session = flist.session()
    request = session.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    try:
        charname = soup.find('span', {'class', 'charname'}).text
        
        found = _get_side_info(soup, 'statbox')
        
        character = Character(charname)
        
        print(charname)
        for key, value in found:
            _key = key.lower().replace(' ', '_')
            # print(_key, f"'{value}'")
            character.set_attribute(_key, value)
            
            
        found = _get_tab_info(soup, 'infodatabox')
        for key, value in found:
            # print(key, f"'{value}'")
            # print(key.lower().replace(' ', '_'), f"'{value}'")
            _key = key.lower().replace(' ', '_')
            character.set_attribute(_key, value)
            
        return character
    
    # todo: info
    # todo: kinks
    
    
    except:
        return None
        
        
    
    
    
    
