import flist


class Note:
    
    def __init__(self, _id, title, sender, receiver, folder, date):
        self.note_id = _id 
        self.title = title
        self.sender = sender 
        self.receiver = receiver
        
        self.folder = folder
        self.date = date
        
    def show(self):
        return flist.notes.get_note_text(self.note_id)
    
    def delete(self):
        return flist.notes.delete_note([self.note_id])
    
    def reply(self, message:str):
        return flist.notes.send_note(self.sender, self.receiver, f"re:{self.title}", message)

    def __repr__(self):
        return f"Title:'{self.title}' ({self.note_id}) from:'{self.sender}' to:'{self.receiver}' ({self.date})"
    
    # TODO: Save messages
