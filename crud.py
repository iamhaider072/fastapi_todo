from sqlalchemy.orm import Session 
from database import  User,Todo



def create_todo(db:Session,title:str,description:str):
    todo=Todo(title=title,description=description)
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo



def get_todos(db:Session,skip:int=0,limit:int=10):
    return db.query(Todo).offset(skip).limit(limit).all()

def get_todo(db:Session,todo_id:int):
    return db.query(Todo).filter(Todo.id==todo_id).first()

