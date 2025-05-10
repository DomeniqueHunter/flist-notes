
import requests
from bs4 import BeautifulSoup

_session = None
_ticket = None
_account = None
_password = None
_proxies = {}
_timeout = None


def login(username:str, password:str, proxies:dict={}, timeout:int=10):
    global _session, _account, _password, _proxies, _timeout
    _account = username
    _password = password
    _session = _session or requests.Session()
    _proxies = _proxies or proxies
    _timeout = _timeout or timeout 
    # can we automaticly set the timeout for ALL requests in all components?
    # maybe we need a send_request function?
    
    if proxies:
        _session.proxies.update(_proxies)
        
    index_response = _session.get('https://www.f-list.net', timeout=_timeout)
    
    soup = BeautifulSoup(index_response.text, 'html.parser')
    
    # get csrf
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']    
    
    # login payload
    payload = {'csrf_token': csrf_token, 'username': username, 'password': password}
    
    response = _session.post('https://www.f-list.net/action/script_login.php', data=payload, timeout=_timeout)
    
    return response


def get_ticket(username:str="", password:str=""):
    global _ticket, _account, _password
    _account = _account or username
    _password = _password or password
    
    payload = {"account": username, "password": password}
    response = _session.post("https://www.f-list.net/json/getApiTicket.php", data=payload)
    _ticket = response.json()["ticket"]
    
    return _ticket


def account():
    return _account


def session():
    return _session


def ticket():
    if not _ticket and _account and _password:
        get_ticket(_account, _password)
        
    return _ticket

