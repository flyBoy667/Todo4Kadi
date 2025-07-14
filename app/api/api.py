from fastapi import APIRouter
from app.api.routers.todo_router import todo_router

api_router = APIRouter()

api_router.include_router(todo_router, prefix="/todos", tags=["todos"])
