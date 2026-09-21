from datetime import datetime

from pydantic import BaseModel, PositiveInt
from pydantic import ValidationError
from typing import Annotated, Literal
from annotated_types import Gt,Ge,Le
from pydantic import StringConstraints


# todo 1개
class TodoItem(BaseModel):
    id:int
    title:str
    completed:bool
    important:bool