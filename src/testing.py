
import config
import flist


def test():
    # login
    request = flist.login.login(config.USER, config.PASSWORD)
    t = flist.login.get_ticket()
    print(t)
    
    # test char..
    character = flist.characters.get_character("")
    print(character)
    
    # test friendrequests
    friend_requests = flist.friends.get_friend_requests()
    print(friend_requests)
    
    # code = flist.friends.accept(request_id=1234)
    # code = flist.friends.deny(request_id=4321)
    # flist.friends.send("you", "other")    
    
    # get characters    
    flist.characters.characters.find_characters(request.content.decode('utf-8'))
    
    conv = flist.notes.Conversations(conversation_root_path=config.CONVERSATIONS_PATH)
    conv.get_in_out_boxes()
    conv.save()
    
    for i, conversation in enumerate(conv.parse_conversations()):
        print(i, conversation)


if __name__ == "__main__":
    test()
