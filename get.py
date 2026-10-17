from fastapi import APIRouter, HTTPException

from store import get_note

router = APIRouter()


@router.get("/notes/{note_id}")
def read_note(note_id: str):
    note = get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
