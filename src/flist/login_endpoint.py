
import requests
from bs4 import BeautifulSoup

_session = None

def login(username, password): 
    request = requests.get('https://www.f-list.net')
    soup = BeautifulSoup(request.text, 'html.parser')
    
    # get csrf
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    
    
    # login payload
    payload = {'csrf_token': csrf_token, 'username': username, 'password': password}
    
    global _session
    _session = requests.session()
    
    request = _session.post('https://www.f-list.net/action/script_login.php', data=payload)
    
    return request


def session():
    return _session

