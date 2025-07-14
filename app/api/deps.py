from typing import Annotated
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends
from app.db.base import engine


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]