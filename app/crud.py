from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from . import models, schemas
from utils.pwd_incriptor import hash_pwd, verify_pwd
from typing import Annotated
from datetime import datetime, timedelta
from utils.oauth2 import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES



async def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).all()


async def create_todo(db: Session, item: schemas.Todo):
    db_todo = models.Todo(**item.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

async def create_user(db: Session, user: schemas.User):
    user_query  = db.query(models.User).filter(models.User.email == user.email).first()

    if user_query is None:
        user.password = hash_pwd(user.password)
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"user with {user.email} already exits")

# def login_user(db: Session, user: schemas.UserLogin, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
async def login_user(db: Session, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_query  = db.query(models.User).filter(models.User.email == form_data.username).first()

    if user_query is not None:
        if verify_pwd(form_data.password, user_query.password):
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(data={"sub": form_data.username}, expires_delta=access_token_expires)
            return {"access_token": access_token, "token_type": "bearer"}
        


        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid password or email")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with{form_data.username} does't exist")


def _():
    ...