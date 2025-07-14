from app.db.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    status = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="todos")
