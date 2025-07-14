from fastapi import APIRouter
from app.api.routers.todo_router import todo_router
from app.api.routers.user_router import user_router

api_router = APIRouter()

api_router.include_router(todo_router, prefix="/todos", tags=["todos"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
