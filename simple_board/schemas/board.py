# 게시글을 삽입: userId,
# 게시글 조회: userId, title, body, id
from pydantic import BaseModel
from datetime import datetime

class BoardCreate(BaseModel):
    user_id: int
    title: str
    contents:str


class BoardUpdate(BaseModel):
    title:str|None = None
    contents:str|None=None

class BoardResponse(BaseModel):
    id:int
    title: str
    contents:str
    user_id: int
    created_at: datetime


class BoardPageResponse(BaseModel):
    items:list[BoardResponse]
    total:int
    page:int
    size:int
    total_pages:int



class Comment(BaseModel):
    
    postId: int
    id: int
    name: str
    email: str
    body:str
  

