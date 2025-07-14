from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import SessionDep
from app.schemas.todo_schemas import TodoCreate, TodoUpdate, TodoRead
from app.models import Todo
from app.db.base import engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

todo_router = APIRouter(prefix="/todo", tags=["todo"])


@todo_router.get("/", response_model=List[TodoRead])
def read_all_todos(session: SessionDep):
    todos = session.query(Todo).all()

    if not todos:
        return []

    return todos


@todo_router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, session: SessionDep):
    try:
        todo = Todo(
            title=todo.title,
            description=todo.description,
            is_completed=False,
            user_id=todo.user_id,
        )
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Todo already exists")


@todo_router.get("/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, session: Session = Depends(SessionDep)):
    todo = session.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@todo_router.put("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoUpdate, session: Session = Depends(SessionDep)):
    todo = session.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = todo.title
    todo.description = todo.description
    todo.is_completed = todo.is_completed
    session.commit()
    session.refresh(todo)
    return todo


@todo_router.delete("/{todo_id}", response_model=TodoRead)
def delete_todo(todo_id: int, session: Session = Depends(SessionDep)):
    todo = session.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return todo
