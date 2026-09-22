from pydantic import BaseModel

class TaskInsert(BaseModel):
    id:int
    text:str
    done:bool

