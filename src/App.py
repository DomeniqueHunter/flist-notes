
import config
import flist


def main():
    request = flist.login(config.USER, config.PASSWORD)
    # print(request.content)
    
    flist.characters.find_characters(request.content.decode('utf-8'))
    
    notes = flist.get_inbox()
    print(notes[0])
    print(notes[0].show())
    
    status = flist.send_note(dest, source, title, text)
    print(status, status.text)
    
    status = flist.notes.delete_note([notes[0].note_id])
    print(status, status.text)
    
if __name__ == "__main__":
    main()
