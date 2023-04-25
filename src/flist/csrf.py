
from bs4 import BeautifulSoup
import flist

_csrf_token = None

def get_csrf_token(page:str) -> str:
    global _csrf_token
    
    if _csrf_token:
        return _csrf_token
    
    # meta csrf token
    session = flist.session()
    request = session.get(page)
    soup = BeautifulSoup(request.text, 'html.parser')
    _csrf_token = soup.find('meta', {'id': 'flcsrf-token'})['content']
    
    return _csrf_token