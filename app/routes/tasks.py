from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import TaskCreate, TaskUpdate
from app.services import task_service
from app.security import get_current_user

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return task_service.create_task_service(task, current_user, db)

@router.get("/tasks")
def get_tasks(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return task_service.get_tasks_service(current_user, db)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return task_service.update_task_service(task_id, task, current_user, db)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return task_service.delete_task_service(task_id, current_user, db)

