import flist
from flist.time.time import ftime


class Note:
    
    def __init__(self, _id, title, sender, receiver, folder, date):
        self.note_id = _id 
        self.title = title
        self.sender = sender 
        self.receiver = receiver
        
        self.folder = folder
        self.date = ftime(date)
        
        self.text = None
        self.deleted_on_server = False
        
    def show(self, force_dl=False):
        if not self.text or force_dl:
            print(f'downloading note text {self.note_id}')
            self.text = flist.notes.get_note_text(self.note_id) 
        
        return self.text
    
    def note(self):
        note = f"\ntitle: {self.title}\nform: {self.sender} to: {self.receiver}\ndate: {self.date}\n"
        note += "-------------------------------------------\n"
        note += self.show() + "\n"
        note += "-------------------------------------------\n\n"
        return note
    
    def delete(self):
        if not self.deleted_on_server:
            self.deleted_on_server = True
            return flist.notes.delete_note([self.note_id])
        return None
    
    def flag_deleted(self):
        if not self.deleted_on_server:
            self.deleted_on_server = True
            return False
        
        return self.deleted_on_server
            
    
    def reply(self, message:str):
        return flist.notes.send_note(self.sender, self.receiver, f"re:{self.title}", message)

    def __repr__(self):
        return f"Title:'{self.title}' ({self.note_id}) from:'{self.sender}' to:'{self.receiver}'"
    
    def __eq__(self, other):
        return self.note_id == other.note_id
    
