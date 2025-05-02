
from bs4 import BeautifulSoup
import flist


def get_friend_list(character:str) -> list:
    session = flist.session()
    char = flist.characters.get_character(character)
    
    headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Host": "www.f-list.net",
        }
    
    data = {
            'csrf_token': flist.csrf.get_csrf_token('https://www.f-list.net'),
            "character_id": char.id
        }
    
    response = session.post('https://www.f-list.net/json/profile-friends.json', headers=headers, data=data) 
    
    return response.json()["friends"]


def send_friend_request(source_character:str, target_character:str):
    session = flist.session()
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Host": "www.f-list.net",
        }
    
    data = {
        "account": flist.login.account(),
        "ticket": flist.login.ticket(),
        "source": source_character, 
        "target": target_character,
        }
    
    response = session.post('https://www.f-list.net/json/api/request-send2.php', headers=headers, data=data)
    
    return response.json()


def get_friend_requests() -> list:
    session = flist.session()
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Host": "www.f-list.net",
        }
    
    data = {
        "account": flist.login.account(),
        "ticket": flist.login.ticket()
        }
    
    response = session.post('https://www.f-list.net/json/api/request-list.php', headers=headers, data=data)
    
    return response.json()["requests"]


def accept_friend_request(request_id:int):
    session = flist.session()
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Host": "www.f-list.net",
        }
    
    data = {
        "account": flist.login.account(),
        "ticket": flist.login.ticket(),
        'request_id': request_id
        }
    
    response = session.post('https://www.f-list.net/json/api/request-accept.php', headers=headers, data=data)
    return response.status_code


def deny_friend_requst(request_id:int):
    session = flist.session()
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Host": "www.f-list.net",
        }
    
    data = {
        "account": flist.login.account(),
        "ticket": flist.login.ticket(),
        'request_id': request_id
        }
    
    response = session.post('https://www.f-list.net/json/api/request-deny.php', headers=headers, data=data)
    return response.status_code


def test():
    print("Test") 


if __name__ == "__main__":
    test()
