
from bs4 import BeautifulSoup
import flist


def send_friend_request():
    pass


def get_friend_requests():
    pass


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


def accept_friend_request():
    pass


def decline_friend_requst():
    pass


def test():
    print("Test") 


if __name__ == "__main__":
    test()
