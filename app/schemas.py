

from pydantic import BaseModel, EmailStr


class Todo(BaseModel):
    title: str
    

class User(BaseModel):
    username: str
    email : EmailStr
    password : str

class UserLogin(User):
    username: str| None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None