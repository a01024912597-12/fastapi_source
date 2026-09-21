
from fastapi import APIRouter
from models.model import TodoItem

todo_router = APIRouter(prefix="/todos")

todos = [
    {
        "id": 1,
        "title": "react 기초 알아보기",
        "completed": True,
        "important": True
    },
    {
        "id": 2,
        "title": "컴포넌트 스타일링해 보기",
        "completed": True,
        "important": False
    },
    {
        "id": 3,
        "title": "일정관리 앱 만들어보기",
        "completed": False,
        "important": False
    },
]

# 딕셔너리 리스트를 TodoItem 객체 리스트로 변환
todo_items = [TodoItem(**todo) for todo in todos]


# 전체 조회
@todo_router.get("/")
async def get_todos():
    return {"todos": todo_items}


# 쿼리 매개변수 조회: /todos/get?id=1
@todo_router.get("/get")
async def get_query_todo(id: int):
    for todo in todo_items:
        if todo.id == id:
            return {"todo": todo}

    return {"todo": "todo를 찾을 수 없습니다"}


# 경로 매개변수 조회: /todos/1
# @todo_router.get("/{id}")
# async def get_todo(id: int):
#    for todo in todo_items:
#        if todo.id == id:
#            return {"todo": todo}

#    return {"todo": "todo를 찾을 수 없습니다"}


# 추가
@todo_router.post("/")
async def post_todo(todo: TodoItem):
    todo_items.append(todo)
    return {"todos": todo_items}


# 수정
@todo_router.put("/{todo_id}")
async def put_todo(todo_id: int, update_todo: TodoItem) -> dict:
    for todo in todo_items:
        if todo.id == todo_id:
            todo.title = update_todo.title
            todo.completed = update_todo.completed
            todo.important = update_todo.important

            return {"todo": todo}

    return {"todo": "todo를 찾을 수 없습니다."}


# 삭제
@todo_router.delete("/{todo_id}")
async def delete_todo(todo_id: int) -> dict:
    for todo in todo_items:
        if todo.id == todo_id:
            todo_items.remove(todo)
            return {"todo_items": todo_items}

    return {"todo": "todo를 찾을 수 없습니다."}