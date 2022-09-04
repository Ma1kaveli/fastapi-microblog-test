# from fastapi_users import schemas
# import uuid


# class User(schemas.BaseUser[uuid.UUID]):
#     pass


# class UserCreate(schemas.BaseUserCreate):
#     pass


# class UserUpdate(schemas.BaseUserUpdate):
#     pass
from pydantic import BaseModel

class UserRegistration(BaseModel):
    name: str
    email: str
    hashed_password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.com",
                "hashed_password": "weakpassword"
            }
        }

class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }