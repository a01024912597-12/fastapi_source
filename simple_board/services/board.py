# CRUD 작업
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select
from repository.models.board import Board
from schemas.board import BoardCreate, BoardUpdate
from exceptions.board import BoardNotFoundException
import math
from repository.models.comment import Comment
from repository.models.user import User
from exceptions.user import UserCreditialsException

def create(db:Session, data:BoardCreate, current_user:User):
    # 스키마 => 테이블 연결 모델
    board = Board(title=data.title, contents=data.contents, user_id=current_user.user_id)
    db.add(board)
    db.commit()
    db.refresh(board)
    return board



def update(db:Session, data:BoardUpdate, id:int, current_user:User):
    # 수정할 대상 찾기
    board = db.get(Board, id)

    if board is None:
        BoardNotFoundException

    # 로그인 사용자 == 작성자 이냐?
    if board.user_id != current_user.user_id:
        raise UserCreditialsException

    # title 만 수정 or contents 만 수정 or title, contents 둘다 수정
    if data.title is not None:
        board.title = data.title

    if data.contents is not None:
        board.contents = data.contents

    db.commit()
    return id

# id 와 일치하는 board 하나 조회
def select_one(db:Session, id:int):
    stmt = select(Board).options( 
        selectinload(Board.user), # 게시글 작성자 정보
        selectinload(Board.comments).selectinload(Comment.user), # 댓글+댓글작성자
        ).where(Board.id==id)

    board = db.scalar(stmt)

    if board is None:
        BoardNotFoundException
    return board

def recentPosts(db:Session):
    return db.query(Board).order_by(Board.created_at.desc()).limit(4).all()
    # 최신 게시물 4개 추출



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
def delete(db:Session, id:int, current_user:User):
    # 삭제할 대상 찾기
    board = db.get(Board,id)
    if board is None:
        BoardNotFoundException

    if board.user_id != current_user.user_id:
        raise UserCreditialsException

    if board is None:
        db.delete(board)
        db.commit()
        return id
