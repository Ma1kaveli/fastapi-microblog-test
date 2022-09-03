from core.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    created_at = Column(DateTime)
    user = Column(Integer, ForeignKey("users.id"))
    user_id = relationship("User")