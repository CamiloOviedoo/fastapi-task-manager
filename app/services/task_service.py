from app.models import Task

def create_task_service(task, current_user, db):
    new_task = Task(title=task.title, completed=task.completed, user_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks_service(current_user, db):
    return db.query(Task).filter(Task.user_id == current_user.id).all()
    
def update_task_service(task_id, task, current_user, db):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    
    if not db_task:
        return {"detail": "Task not found"}
    
    db_task.title = task.title
    db_task.completed = task.completed
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task_service(task_id, current_user, db):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    
    if not db_task:
        return {"detail": "Task not found"}
    
    db.delete(db_task)
    db.commit()
    return {"detail": "Task deleted successfully"}