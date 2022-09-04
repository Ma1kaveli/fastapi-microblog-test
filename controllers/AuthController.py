from sqlalchemy.orm import Session

from models.user.model import User 
from schemas import UserSchemas
from helpers import auth_helpers
from core.hashing import Hasher

def registration(db: Session, item: UserSchemas.UserRegistration):
    check_user = auth_helpers.check_user(db, item.email)
    item.hashed_password = Hasher.get_password_hash(item.hashed_password)
    if check_user['found']:
        return False
    user = User(**item.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db: Session, item: UserSchemas.UserLogin):
    check_user = auth_helpers.check_user(db, item.email)
    if check_user['found'] == False:
        return False
    if Hasher.verify_password(item.password, check_user['user'].hashed_password) == False:
        return False
    return check_user['user']