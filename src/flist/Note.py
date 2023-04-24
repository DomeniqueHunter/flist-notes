import flist


class Note:
    
    def __init__(self, id, title, sender, receiver, folder, date):
        self.note_id = id 
        self.title = title
        self.sender = sender 
        self.receiver = receiver
        
        self.folder = folder
        self.date = date
        
    def show(self):
        return flist.get_note_text(self.note_id)

    def __repr__(self):
        return f"Title:'{self.title}' ({self.note_id}) from:'{self.sender}' to:'{self.receiver}' ({self.date})"
    
    # TODO: Save messages