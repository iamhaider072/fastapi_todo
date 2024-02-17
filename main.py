from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud
from database import SessionLocal, engine,TodoCreate,Base

app = FastAPI()


@app.post("/todos/")
def create_todo(todo:TodoCreate, db: Session = Depends(SessionLocal)):
    return crud.create_todo(db, title=todo.title, description=todo.description)

@app.get("/todos/")
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return crud.get_todos(db, skip=skip, limit=limit)

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(SessionLocal)):
    return crud.get_todo(db, todo_id=todo_id)

# Create the database tables when the application starts
def init_db():
    Base.metadata.create_all(bind=engine)



init_db()
