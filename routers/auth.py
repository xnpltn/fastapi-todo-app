from fastapi import APIRouter, Depends
from app import schemas
from sqlalchemy.orm import Session
from app.crud import create_user, login_user
from app.database import get_db
from utils.pwd_incriptor import hash_pwd, verify_pwd
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Login"]
)



@router.post("/signup")
async def signup(user: schemas.User ,db: Session = Depends(get_db)):
    return await create_user(db=db, user=user)
    

# user: schemas.UserLogin
@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    return await login_user(db=db, form_data=form_data)