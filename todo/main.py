from fastapi import FastAPI
from routes.todo import todo_router

app = FastAPI()
app.include_router(todo_router)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# # http://127.0.0.1:8000/todos/1
# @app.get("/todos/{id}")
# def read_item(id: int):
#     return {"id": id}