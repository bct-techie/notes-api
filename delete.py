from fastapi import APIRouter, HTTPException, status

from store import delete_note

router = APIRouter()


@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_note(note_id: str):
    if not delete_note(note_id):
        raise HTTPException(status_code=404, detail="Note not found")
