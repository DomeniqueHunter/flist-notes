
import flist
import pathlib
import config
import pickle
from .Conversation import Conversation


class Conversations:
    
    def __init__(self):
        self.session = flist.session()
        
        self.all_conversations = self.load()
    
    def add_to_dict(self, key:str, value):
        if key not in self.all_conversations:
            self.all_conversations[key] = Conversation(key)
    
        self.all_conversations[key].append(value, sort=False)
    
    def load(self):
        try:
            with open(f'{config.CONVERSATIONS_PATH}/conv.pickle', 'rb') as handle:
                conv = pickle.load(handle)
                return conv
            
        except Exception as e:
            print(e)
            return {}
        
    def save(self):
        if self.all_conversations and len(self.all_conversations) > 0:
            pathlib.Path(config.CONVERSATIONS_PATH).mkdir(parents=True, exist_ok=True)
    
            with open(f'{config.CONVERSATIONS_PATH}/conv.pickle', 'wb') as handle:
                pickle.dump(self.all_conversations, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    def save_conversation(self, key:str, filename:str):
        if key in self.all_conversations:
            with open(f'{config.CONVERSATIONS_PATH}/{filename}', 'w') as f:
                for note in self.all_conversations[key].conversation:
                    f.write(note.note())
    
    def get_conv(self, key):
        if key in self.all_conversations:
            return self.all_conversations[key]
    
    def get_in_out_boxes(self, chunk_size=25):
        offset = 0
        in_notes, in_total = flist.notes.get_inbox(offset=offset, amount=chunk_size)
        while len(in_notes) < in_total:
            offset += chunk_size
            notes, _ = flist.notes.get_inbox(offset=offset, amount=chunk_size)
            in_notes += notes
    
        offset = 0
        out_notes, out_total = flist.notes.get_outbox(offset=offset, amount=chunk_size)
        while len(out_notes) < out_total:
            offset += chunk_size
            notes, _ = flist.notes.get_outbox(offset=offset, amount=chunk_size)
            out_notes += notes
    
        return in_notes, out_notes

    def parse_conversations(self):
        """
            gets all notes from server and creates conversations
        """
        in_notes, out_notes = self.get_in_out_boxes(chunk_size=25)
            
        for note in in_notes:
            key = f'{note.sender.lower()}_{note.receiver.lower()}'
            self.add_to_dict(key, note)
    
        for note in out_notes:
            key = f'{note.receiver.lower()}_{note.sender.lower()}'
            self.add_to_dict(key, note)
    
        for key, value in self.all_conversations.items():
            # print(key, len(value))
            # all_conversations[key] = sorted(value, key=lambda n: n.note_id)
            self.all_conversations[key].sort()
    
        self.save()
    
        return self.all_conversations




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            