
import flist
import pathlib
import pickle
from .Conversation import Conversation


class Conversations:

    def __init__(self, conversation_root_path=None):
        self.conversation_root_path = conversation_root_path
        self.session = flist.session()

        self.all_conversations = self.load()

    def add_to_dict(self, key:str, value):
        if key not in self.all_conversations:
            self.all_conversations[key] = Conversation(key)

        self.all_conversations[key].append(value, sort=False)

    def load(self):
        try:
            with open(f'{self.conversation_root_path}/conv-{flist.login.account().lower()}.pickle', 'rb') as handle:
                conv = pickle.load(handle)
                return conv

        except Exception as e:
            print(e)
            return {}

    def save(self):
        """
        saves all Conversations in one pickle file.
        """
        if self.all_conversations and len(self.all_conversations) > 0:
            pathlib.Path(self.conversation_root_path).mkdir(parents=True, exist_ok=True)

            with open(f'{self.conversation_root_path}/conv-{flist.login.account().lower()}.pickle', 'wb') as handle:
                pickle.dump(self.all_conversations, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def save_conversation(self, key:str, filename:str):
        """
        saves one onversation at a time to a txt file in human readable form
        """
        if key in self.all_conversations:
            with open(f'{self.conversation_root_path}/{filename}', 'w') as f:
                for note in self.all_conversations[key].conversation:
                    f.write(note.note())

    def get_conv(self, key):
        if key in self.all_conversations:
            return self.all_conversations[key]

    def get_in_out_boxes(self, chunk_size=25):
        """
        reads in and out boxes from server and stores them in lists
        """
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
            sender = note.sender.lower().replace(" ", "_")
            receiver = note.receiver.lower().replace(" ", "_")
            key = f'{sender}_{receiver}'
            self.add_to_dict(key, note)

        for note in out_notes:  #
            sender = note.sender.lower().replace(" ", "_")
            receiver = note.receiver.lower().replace(" ", "_")
            key = f'{receiver}_{sender}'
            self.add_to_dict(key, note)

        for value in self.all_conversations.values():
            value.sort()

        self.save()

        return self.all_conversations

