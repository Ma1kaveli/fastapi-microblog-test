from fastapi import APIRouter
from .post import post
from .auth import auth


api = APIRouter()

api.include_router(post, prefix="/posts", tags=["post"])
api.include_router(auth, prefix="/auth", tags=["auth"])