
import config
import flist


def notes():
    print('0: back\n1: Inbox\n2: Outbox\n3: Trash\nr <nr>: read note\nq: quit')
    while True:
        cmd = input('> ')
        
        if cmd == 'q':
            exit()
        if cmd == '0':
            print('\n...back..\n\n')
            break
        
        if cmd == '1':
            inbox_notes, _ = flist.notes.get_inbox()
            for note in inbox_notes:
                print(note)
            print()
            
        if cmd == '2':
            outbox_notes, _ = flist.notes.get_outbox()
            for note in outbox_notes:
                print(note)
            print()
        
        if cmd.startswith('r'):
            try:
                _, nr = cmd.split(' ')
                print(flist.notes.get_note_text(nr))
                print()
            except:
                pass


def main():
    
    # login
    request = flist.login.login(config.USER, config.PASSWORD)
    
    # get characters    
    flist.characters.characters.find_characters(request.content.decode('utf-8'))
    exit()
    print('h: help\nq: quit')
    while True:
        cmd = input('> ')
        
        if cmd == 'q' or cmd == 'Q' or cmd == 'quit' or cmd == 'exit':
            exit()
            
        if cmd == 'h':
            print('q: quit\nn: notes')
            
        if cmd == 'n':
            notes()
            
        print(cmd)


def test():
    # login
    request = flist.login.login(config.USER, config.PASSWORD)
    t = flist.login.get_ticket()
    print(t)
    
    # test char..
    character = flist.characters.get_character("")
    
    # test friendrequests
    friend_requests = flist.friends.get_friend_requests()
    print(friend_requests)
    
    # code = flist.friends.accept(request_id=1234)
    # code = flist.friends.deny(request_id=4321)
    # flist.friends.send("you", "other")    
    
    exit()
    
    # get characters    
    flist.characters.characters.find_characters(request.content.decode('utf-8'))
    
    conv = flist.notes.Conversations()
    conv.get_in_out_boxes()
    conv.save()
    
    for i, conversation in enumerate(conv.parse_conversations()):
        print(i, conversation)

  
if __name__ == "__main__":
    # main()
    test()
