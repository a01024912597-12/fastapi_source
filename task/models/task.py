from pydantic import BaseModel

class TaskInsert(BaseModel):
    text:str
    done:bool


class Task(TaskInsert):
    id:int