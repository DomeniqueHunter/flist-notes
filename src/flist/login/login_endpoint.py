
import requests
from bs4 import BeautifulSoup

_session = None
_ticket = None
_account = None
_password = None


def login(username, password): 
    request = requests.get('https://www.f-list.net')
    
    soup = BeautifulSoup(request.text, 'html.parser')
    
    # get csrf
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']    
    
    # login payload
    payload = {'csrf_token': csrf_token, 'username': username, 'password': password}
    
    global _session, _account, _password
    _account = username
    _password = password
    _session = requests.session()
    # _session.headers.update({"User-Agent" : config.USER_AGENT})
    
    response = _session.post('https://www.f-list.net/action/script_login.php', data=payload)
    
    return response


def get_ticket(username:str, password:str):
    payload = {"account": username, "password": password}
    response = requests.post("https://www.f-list.net/json/getApiTicket.php", data=payload)
    ticket = response.json()["ticket"]
    
    global _ticket, _account, _password
    _account = username
    _password = password
    _ticket = ticket
    
    return ticket


def account():
    return _account


def session():
    return _session


def ticket():
    if not _ticket and _account and _password:
        get_ticket(_account, _password)
        
    return _ticket

