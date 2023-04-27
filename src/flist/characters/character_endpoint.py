
import flist
import re
from bs4 import BeautifulSoup



def get_character(character_name:str):
    url = f'https://www.f-list.net/c/{character_name}'
    
    session = flist.session()
    request = session.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    
    charname = soup.find('span', {'class', 'charname'}).text
    statbox = soup.find('div', {'class', 'statbox'})
    
    raw_text = str((statbox))
    
    # print(raw_text.replace('\n', '').replace('\r', '').replace('\t', ' ').replace('<br/>', '\n'))
    
    regex = '<span class="taglabel">([a-zA-Z0-9 \/]+)<\/span>:[ ]+([a-zA-Z0-9 \/,._-]+)'
    pattern = re.compile(regex)
    
    found = re.findall(pattern, raw_text)
    
    for key, value in found:
        print(key, f"'{value}'")
        
        
        
    
    
    
    
