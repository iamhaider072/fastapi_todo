from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,session
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "postgresql://iamhaider072:iuYSL4wXG5xk@ep-aged-waterfall-a52my4g0.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Pydantic Model
class TodoCreate(BaseModel):
    title: str
    description: str




#models.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    todos=relationship("Todo", back_populates="owner_id")


class Todo(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    description=Column(String,index=True)

    owner_id=relationship("User",back_populates="todos")












