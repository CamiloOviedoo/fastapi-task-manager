from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    contraseña: str

class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    
    
class UserLogin(BaseModel):
    username: str
    contraseña: str
    

class TaskUpdate(BaseModel):
    title: str
    completed: bool     