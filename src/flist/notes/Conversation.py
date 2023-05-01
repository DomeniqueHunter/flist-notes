import flist
from flist.notes.Note import Note




class Conversation:
    
    def __init__(self, label:str, conv:list=None):
        self.conversation = conv if conv else []
        self.label = label
        
    def sort(self):
        self.conversation.sort(key=lambda x: x.note_id, reverse=False)
        
    def delete(self):
        flist.notes.delete_note([n.note_id for n in self.conversation if not n.flag_deleted()])
            
    def show(self, _all=False):
        for note in self.conversation:
            if _all:
                print(note.note())
            else:
                print(note)
                
    def append(self, note:Note, sort=True):
        if isinstance(note, Note) and note not in self.conversation:
            self.conversation.append(note)
        
        if sort:
            self.sort()
            
    def save(self):
        flist.notes.converstaion.save_conversation(self.conversation, self.label)
            
    def __len__(self):
        return len(self.conversation)


def test():
    c = Conversation('test')
    print(c.conversation)                
                
if __name__ == "__main__":
    test()