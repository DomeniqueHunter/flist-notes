import flist


def add_to_dict(_dict:dict, key:str, value):
    if key not in _dict:
        _dict[key] = []

    _dict[key].append(value)


def get_in_out_boxex(amount=100):
    in_notes = flist.notes.get_inbox(amount=amount)
    out_notes = flist.notes.get_outbox(amount=amount)

    return in_notes, out_notes


def conversations(in_notes, out_notes):
    all_notes = {}
    for note in in_notes:
        key = f'{note.sender.lower()}_{note.receiver.lower()}'
        add_to_dict(all_notes, key, note)

    for note in out_notes:
        key = f'{note.receiver.lower()}_{note.sender.lower()}'
        add_to_dict(all_notes, key, note)

    for key, value in all_notes.items():
        print(key, len(value))
        all_notes[key] = sorted(value, key=lambda n: n.note_id)

    return all_notes


def save(conversation:list, filename:str):
    # write content of list to file
    with open(filename, 'w') as f:
        for note in conversation:
            f.write(note.note())


