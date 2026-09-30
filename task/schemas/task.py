
from pydantic import BaseModel

class TaskCreate(BaseModel):    
    text:str
    done:bool

class TaskUpdate(BaseModel):    
    text:str|None=None
    done:bool|None=None

class Task(TaskCreate):
    id:int



class TaskPageResponse(BaseModel):
    items: list[Task]
    total:int
    total_pages:int
    page:int
    size:int



