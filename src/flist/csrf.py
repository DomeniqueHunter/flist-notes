
from bs4 import BeautifulSoup
import requests


def get_csrf_token(page:str) -> str:
    # meta csrf token
    request = requests.get(page)
    soup = BeautifulSoup(request.text, 'html.parser')
    csrf = soup.find('meta', {'id': 'flcsrf-token'})['content']
    
    return csrf