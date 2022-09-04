from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from core import db


class User(db.Base, SQLAlchemyBaseUserTable):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)