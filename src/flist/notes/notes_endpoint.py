
from bs4 import BeautifulSoup
import flist
from .Note import Note


def get_inbox(offset:int=0, amount:int=10):
    notes_data = get_notes(offset, amount, 1)
    total_notes = notes_data['total']
    notes_json = notes_data['notes']
    
    notes_list = []
    
    for note in notes_json:
        note_object = Note(note['note_id'], note['title'], note['source_name'], note['dest_name'], note['folder_id'], note['datetime_sent'])
        notes_list.append(note_object)
        # print(note_object)        
    
    return notes_list, total_notes

    
def get_outbox(offset:int=0, amount:int=10):
    notes_data = get_notes(offset, amount, 2)
    total_notes = notes_data['total']
    notes_json = notes_data['notes']
    
    notes_list = []
    
    for note in notes_json:
        note_object = Note(note['note_id'], note['title'], note['source_name'], note['dest_name'], note['folder_id'], note['datetime_sent'])
        notes_list.append(note_object)
        # print(note_object)        
    
    return notes_list, total_notes

    
def get_notes(offset:int, amount:int, box:int):
    session = flist.session()
    return session.get(f"https://www.f-list.net/json/notes-get.json?offset={offset}&amount={amount}&folder={box}").json()


def get_note_text(note_id:int):
    session = flist.session()
    html = session.get(f"https://www.f-list.net/view_note.php?note_id={note_id}").text
    soup = BeautifulSoup(html, 'html.parser')    
    content = soup.find('div', {'class': 'FormattedBlock'})
    
    return content.text


def send_note(dest:str, source:str, title:str, text:str):
    headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Host": "www.f-list.net",
        }
    
    note_data = {
            'csrf_token': flist.csrf.get_csrf_token('https://www.f-list.net'),
            'title': title,
            'message': text,
            'dest': dest,
            'source': flist.characters.characters.character_id(source),
        }
    
    session = flist.session()
    
    return session.post('https://www.f-list.net/json/notes-send.json', headers=headers, data=note_data)


def delete_note(note_ids:list):
    headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Host": "www.f-list.net",
        }
    
    note_data = {
            'csrf_token': flist.csrf.get_csrf_token('https://www.f-list.net'),
            'notes[]': note_ids,
        }
    
    session = flist.session()
    
    return session.post('https://www.f-list.net/json/notes-trash.json', headers=headers, data=note_data)


def empty_trash():
    headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Host": "www.f-list.net",
        }
    
    note_data = {
            'csrf_token': flist.csrf.get_csrf_token('https://www.f-list.net'),
        }
    
    session = flist.session()
    
    return session.post('https://www.f-list.net/json/notes-emptytrash.json', headers=headers, data=note_data)



