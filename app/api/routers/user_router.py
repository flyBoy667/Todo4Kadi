from fastapi import APIRouter, Depends, HTTPException
from app.api.deps import SessionDep
from app.schemas.user_schemas import UserCreate, UserUpdate, UserRead
from app.models import User
from sqlalchemy.exc import IntegrityError

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/", response_model=list[UserRead])
def read_users(session: SessionDep):
    users = session.query(User).all()

    if not users:
        return []
    return users


@user_router.post("/", response_model=UserRead)
def create_user(user: UserCreate, session: SessionDep):
    try:
        user_obj = User(full_name=user.full_name, email=user.email)
        session.add(user_obj)
        session.commit()
        session.refresh(user_obj)
        return user_obj
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")


@user_router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: SessionDep):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserUpdate, session: SessionDep):
    user_obj = session.query(User).filter(User.id == user_id).first()
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    user_obj.full_name = user.full_name
    user_obj.email = user.email
    session.commit()
    session.refresh(user_obj)
    return user_obj


@user_router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: int, session: SessionDep):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return user
