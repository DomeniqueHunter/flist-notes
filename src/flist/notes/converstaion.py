import flist
import pathlib
import config
import pickle


def add_to_dict(_dict:dict, key:str, value):
    if key not in _dict:
        _dict[key] = []

    if value not in _dict[key]:
        _dict[key].append(value)


def get_in_out_boxex(amount=100):
    in_notes = flist.notes.get_inbox(amount=amount)
    out_notes = flist.notes.get_outbox(amount=amount)

    return in_notes, out_notes


def conversations(in_notes, out_notes):
    loaded_conversations = load()

    all_conversations = loaded_conversations if loaded_conversations else {}  # load if file exists
    print(len(all_conversations), 'conversations')

    for note in in_notes:
        key = f'{note.sender.lower()}_{note.receiver.lower()}'
        add_to_dict(all_conversations, key, note)

    for note in out_notes:
        key = f'{note.receiver.lower()}_{note.sender.lower()}'
        add_to_dict(all_conversations, key, note)

    for key, value in all_conversations.items():
        # print(key, len(value))
        all_conversations[key] = sorted(value, key=lambda n: n.note_id)

    save(all_conversations)

    return all_conversations


def save(data:dict):
    if data and len(data) > 0:
        pathlib.Path(config.CONVERSATIONS_PATH).mkdir(parents=True, exist_ok=True)

        with open(f'{config.CONVERSATIONS_PATH}/conv.pickle', 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load() -> dict:
    try:
        with open(f'{config.CONVERSATIONS_PATH}/conv.pickle', 'rb') as handle:
            conv = pickle.load(handle)
            return conv
    except Exception as e:
        print(e)


def save_conversations(conversation:list, filename:str):
    # write content of list to file
    with open(filename, 'w') as f:
        for note in conversation:
            f.write(note.note())

