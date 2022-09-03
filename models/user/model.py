from core.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime)
    is_verify = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)