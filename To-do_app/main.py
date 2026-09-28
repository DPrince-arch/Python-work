import asyncio
from datetime import datetime, timezone, timedelta
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import model
import schema
from database import engine, SessionLocal, get_db

model.Base.metadata.create_all(bind=engine)

CLEANUP_EXPIRATION = timedelta(seconds=30)


def utc_now():
    return datetime.now(timezone.utc)

async def auto_cleanup_todos_loop():
    while True:
        try:
            await asyncio.sleep(5)
            db: Session = SessionLocal()
            try:
                now = utc_now()
                completed_todos = (
                    db.query(model.TodoItem)
                    .filter(model.TodoItem.completed == True)
                    .all()
                )

                expired_todos = []
                for todo in completed_todos:
                    if todo.completed_at:
                        comp_time = todo.completed_at
                        if comp_time.tzinfo is None:
                            comp_time = comp_time.replace(tzinfo=timezone.utc)
                        if (now - comp_time) >= CLEANUP_EXPIRATION:
                            expired_todos.append(todo)
                    else:
                        expired_todos.append(todo)

                for todo in expired_todos:
                    print(f"[AUTO-CLEANUP] 🧹 Deleted completed task #{todo.id}: '{todo.title}'")
                    db.delete(todo)

                if expired_todos:
                    db.commit()
            finally:
                db.close()
        except asyncio.CancelledError:
            print("[AUTO-CLEANUP] Stopped.")
            break
        except Exception as e:
            print(f"[AUTO-CLEANUP ERROR] {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    clean_task = asyncio.create_task(auto_cleanup_todos_loop())
    print("[SYSTEM] Auto-Cleaner background worker started!")
    yield
    clean_task.cancel()


app = FastAPI(title="FastAPI To-Do App", lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Welcome to your To-Do API!"}

@app.post("/todos/", response_model=schema.TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schema.TodoCreate, db: Session = Depends(get_db)):
    new_todo = model.TodoItem(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        priority=todo.priority,
        created_at=utc_now(),
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.get("/todos/", response_model=List[schema.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return db.query(model.TodoItem).order_by(model.TodoItem.id.desc()).all()

@app.get("/todos/{todo_id}", response_model=schema.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return todo

@app.patch("/todos/{todo_id}", response_model=schema.TodoResponse)
def update_todo(
    todo_id: int, 
    todo_update: schema.TodoUpdate, 
    db: Session = Depends(get_db)
):
    db_todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"To-Do item with ID {todo_id} not found"
        )
    update_data = todo_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.post("/todos/{todo_id}/complete", response_model=schema.TodoResponse)
def complete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")

    db_todo.completed = True
    db_todo.completed_at = utc_now()

    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")

    db.delete(db_todo)
    db.commit()
    return None