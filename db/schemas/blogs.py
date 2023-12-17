from typing import List, Any

from pydantic import BaseModel


class PostBase(BaseModel):
    id: int


class PostCreate(BaseModel):
    id: int
    author: Any
    title: str
    content: str
    tags: List[str] = []


class CommentBase(PostBase):
    comment: str
