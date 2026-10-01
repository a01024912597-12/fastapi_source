# CRUD 작업
from sqlalchemy.orm import Session
from repository.models.board import Board
from schemas.board import BoardCreate, BoardUpdate
from exceptions.board import BoardNotFoundException
import math

def create(db:Session, data:BoardCreate):
    # 스키마 => 테이블 연결 모델
    board = Board(title=data.title, contents=data.contents, user_id=data.user_id)
    db.add(board)
    db.commit()
    db.refresh(board)
    return board



def update(db:Session, data:BoardUpdate, id:int):
    # 수정할 대상 찾기
    board = db.get(Board, id)

    if board is None:
        BoardNotFoundException
    # title 만 수정 or contents 만 수정 or title, contents 둘다 수정
    if data.title is not None:
        board.title = data.title

    if data.contents is not None:
        board.contents = data.contents

    db.commit()
    return id

# id 와 일치하는 board 하나 조회
def select_one(db:Session, id:int):
    board = db.get(Board, id)
    if board is None:
        BoardNotFoundException
    return board

# page, size 이용하는 전체 조회
def select_all(db:Session,page:int,size:int):
    query = db.query(Board)

    # 전체 개수
    total = query.count()
    offset = (page - 1) * size
    boards = query.order_by(Board.id.desc()).offset(offset).limit(size).all()
    total_pages = math.ceil(total/size)

    return {
        "items":boards,
        "total":total,
        "page":page,
        "size":size,
        "total_pages": total_pages,
    }

# 삭제
def delete(db:Session, id:int):
    # 삭제할 대상 찾기
    board = db.get(Board,id)
    if board is None:
        BoardNotFoundException

    if board is None:
        db.delete(board)
        db.commit()
        return id
