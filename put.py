from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from store import replace_note

router = APIRouter()


class NoteReplace(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)


@router.put("/notes/{note_id}")
def put_note(note_id: str, body: NoteReplace):
    note = replace_note(note_id, body.title, body.content)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
