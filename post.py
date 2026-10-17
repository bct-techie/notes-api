from fastapi import APIRouter, status
from pydantic import BaseModel, Field

from store import create_note

router = APIRouter()


class NoteCreate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)


@router.post("/notes", status_code=status.HTTP_201_CREATED)
def post_note(body: NoteCreate):
    return create_note(body.title, body.content)
