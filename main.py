from fastapi import FastAPI, Depends, HTTPException, status
from app import models
from routers import auth
from app.database import engine, get_db
from sqlalchemy.orm import Session
from app import schemas, crud
from typing import List
from utils.oauth2 import get_current_user


app = FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)






@app.get("/")
async def hello():
    return {"message": "hello world"}


@app.get("/items")
async def getall(db: Session = Depends(get_db)):
    query =  db.query(models.Todo).all()
    return query

@app.post("/items", response_model=schemas.Todo)
async def create_item_for_user(item: schemas.Todo, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    if item is not None:
        if current_user is not None:
            print(item)
            return await crud.create_todo(db=db, item=item)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Please login in ")
    return HTTPException(status_code=409, detail="something went wrong")





