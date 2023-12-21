from sqlalchemy import Column, String, Integer
from .database import Base
from pydantic import EmailStr

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title:str = Column(String, nullable=False,)




class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title:str = Column(String, nullable=False,)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, nullable=False, unique=True)
    email: EmailStr= Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)

