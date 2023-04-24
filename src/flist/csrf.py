
from bs4 import BeautifulSoup
import flist


def get_csrf_token(page:str) -> str:
    # meta csrf token
    session = flist.session()
    request = session.get(page)
    soup = BeautifulSoup(request.text, 'html.parser')
    csrf = soup.find('meta', {'id': 'flcsrf-token'})['content']
    
    return csrf