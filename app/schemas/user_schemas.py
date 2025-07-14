from typing import Optional
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    id: Optional[int]
    full_name: str
    email: str

class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)

class UserUpdate(UserBase):
    id: int

class UserRead(UserBase):
    id: int
    full_name: str
    email: str
