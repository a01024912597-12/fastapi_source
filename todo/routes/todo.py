from fastapi import APIRouter, HTTPException, status, Depends
from schemas.todo import TodoCreate, TodoUpdate, TodoResponse, TodoPageResponse
from services.todo import create, select, update, delete
from repository.models.todo import Todo
from repository.database import get_db
from sqlalchemy.orm import Session

todo_router = APIRouter(prefix="/todos", tags=['Todos'])

# 사용자의 요청/응답 시 사용할 모델은 schemas 아래
# 추가
@todo_router.post("/")
async def post_todo(data: TodoCreate, db:Session=Depends(get_db))->dict:

    # 서비스의 함수 호출
    # TodoCreate => Todo
    todo = Todo(title=data.title, completed=data.completed, important=data.important)
    new_todo = create(todo=todo, db=db)

    return{"message":f"Todo {new_todo.id} 삽입 성공"}

# 조회
@todo_router.get("/", response_model=TodoPageResponse)
async def get_todos(db:Session=Depends(get_db), completed:bool | None = None, page:int=1, size:int=10)->list[TodoResponse]:

    todos = select(completed, db=db, page=page, size=size)

    return todos

# 수정
@todo_router.put("/{todo_id}")
async def put_todo(todo_id:int, update_todo:TodoUpdate, db:Session=Depends(get_db)) -> dict:


    
    result = update(id=todo_id, data=update_todo, db=db)

    # return {"todo": "todo를 찾을 수 없습니다."}
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="todo를 찾을 수 없습니다.")
    return{"message":f"Todo {result} 수정 성공"}


# 삭제
@todo_router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db:Session=Depends(get_db)) -> dict:

    result = delete(id=todo_id, db=db)

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="todo를 찾을 수 없습니다.")

    return {"message": f"Todo{result} 삭제 성공"}

             


    


# todos = [
#     {
#         "id": 1,
#         "title": "react 기초 알아보기",
#         "completed": True,
#         "important": True
#     },
#     {
#         "id": 2,
#         "title": "컴포넌트 스타일링해 보기",
#         "completed": True,
#         "important": False
#     },
#     {
#         "id": 3,
#         "title": "일정관리 앱 만들어보기",
#         "completed": False,
#         "important": False
#     },
# ]

# # 딕셔너리 리스트를 TodoItem 객체 리스트로 변환
# todo_items = [TodoItem(**todo) for todo in todos]


# # 전체 조회
# @todo_router.get("/", response_model=Todo)
# async def get_todos(completed:bool | None = None)->Todo:
    
#     if completed is None:
#         filtered_todos = todo_items
#     else:
#         filtered_todos = [todo for todo in todo_items if todo.completed == completed]
#     return {"todos": filtered_todos}

# # 쿼리 매개변수 조회: /todos/get?id=1
# @todo_router.get("/get")
# async def get_query_todo(id: int):
#     for todo in todo_items:
#         if todo.id == id:
#             return {"todo": todo}

#     # return {"todo": "todo를 찾을 수 없습니다"}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="todo를 찾을 수 없습니다.")


# # 경로 매개변수 조회: /todos/1
# # @todo_router.get("/{id}")
# # async def get_todo(id: int):
# #    for todo in todo_items:
# #        if todo.id == id:
# #            return {"todo": todo}

# #    return {"todo": "todo를 찾을 수 없습니다"}


# # 추가
# @todo_router.post("/")
# async def post_todo(todo: TodoItem):
#     todo_items.append(todo)

#     create()

#     return{"message":"success"}


# # 수정
# @todo_router.put("/{todo_id}")
# async def put_todo(todo_id: int, update_todo: TodoItem) -> dict:
#     for todo in todo_items:
#         if todo.id == todo_id:
#             todo.title = update_todo.title
#             todo.completed = update_todo.completed
#             todo.important = update_todo.important

#             return {"todo": todo}

#     # return {"todo": "todo를 찾을 수 없습니다."}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="todo를 찾을 수 없습니다.")


# # 삭제
# @todo_router.delete("/{todo_id}", response_model=Todo)
# async def delete_todo(todo_id: int) -> dict:
#     for todo in todo_items:
#         if todo.id == todo_id:
#             todo_items.remove(todo)
#             return {"message":"success"}
            
#             # return {"todo_items": todo_items}

#     # return {"todo": "todo를 찾을 수 없습니다."}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="todo를 찾을 수 없습니다.")