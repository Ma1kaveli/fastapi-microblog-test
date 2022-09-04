from sqlalchemy.orm import Session
from models.post.model import Post
from schemas import PostSchemas


def index(db: Session):
    return db.query(Post).all()

def store(db: Session, item: PostSchemas.PostCreate):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
