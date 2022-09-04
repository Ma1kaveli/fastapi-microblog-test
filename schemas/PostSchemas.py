from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    text: str
    created_at: datetime

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int



class PostCreate(PostBase):
    pass