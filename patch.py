from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from store import get_note, update_note

router = APIRouter()


class NotePatch(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    content: str | None = Field(default=None, min_length=1)


@router.patch("/notes/{note_id}")
def patch_note(note_id: str, body: NotePatch):
    if get_note(note_id) is None:
        raise HTTPException(status_code=404, detail="Note not found")
    updates = body.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    note = update_note(note_id, updates)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
