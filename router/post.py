from typing import List 
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from controllers import PostController
from schemas import PostSchemas
from core.auth_bearer import JWTBearer

post = APIRouter()

@post.get('/', response_model=List[PostSchemas.PostList])
def index(db: Session = Depends(get_db)):
    return PostController.index(db)


@post.post('/', dependencies=[Depends(JWTBearer())])
def store(item: PostSchemas.PostCreate, db: Session = Depends(get_db)):
    return PostController.store(db, item)
    