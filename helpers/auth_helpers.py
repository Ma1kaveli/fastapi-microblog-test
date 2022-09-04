from sqlalchemy.orm import Session
from models.user.model import User 



def check_user(db: Session, email: str):
    user = db.query(User).filter_by(email=email).first()
    if user:
        return {"found": True, "user": user }
    return {"found": False}