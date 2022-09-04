from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from schemas import UserSchemas
from core.auth_handler import signJWT
from controllers import AuthController
from core.auth_bearer import JWTBearer


auth = APIRouter()


@auth.post("/signup")
async def registration(user: UserSchemas.UserRegistration, db: Session = Depends(get_db)):
    if AuthController.registration(db, user) == False:
        return {
            "error": True,
            "msg": 'Error!'
        }
    return signJWT(user.email)


@auth.post("/login")
async def login(user: UserSchemas.UserLogin, db: Session = Depends(get_db)):
    if AuthController.login(db, user) == False:
        return {
            "error": True,
            "msg": 'Error!'
        }
    return signJWT(user.email)


@auth.post("/refresh")
async def refresh():
    pass


@auth.post("/logout", dependencies=[Depends(JWTBearer())])
async def logout():
    pass