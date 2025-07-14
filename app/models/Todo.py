from app.db.base import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    is_completed = Column(Boolean, nullable=False, default=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="todos")
