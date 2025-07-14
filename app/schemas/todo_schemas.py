from typing import Optional
from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    id: Optional[int]
    title: str
    description: str


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    user_id: int = Field(..., gt=0)


class TodoUpdate(TodoBase):
    id: int


class TodoRead(TodoBase):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id: int
