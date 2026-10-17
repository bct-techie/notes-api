from uuid import uuid4

notes: dict[str, dict] = {}


def create_note(title: str, content: str) -> dict:
    note_id = str(uuid4())
    note = {"id": note_id, "title": title, "content": content}
    notes[note_id] = note
    return note


def get_note(note_id: str) -> dict | None:
    return notes.get(note_id)


def replace_note(note_id: str, title: str, content: str) -> dict | None:
    if get_note(note_id) is None:
        return None
    note = {"id": note_id, "title": title, "content": content}
    notes[note_id] = note
    return note


def update_note(note_id: str, updates: dict) -> dict | None:
    note = get_note(note_id)
    if note is None:
        return None
    note.update(updates)
    return note


def delete_note(note_id: str) -> bool:
    if get_note(note_id) is None:
        return False
    del notes[note_id]
    return True
