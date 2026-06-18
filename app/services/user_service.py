from fastapi import HTTPException
from app.models import User
from passlib.context import CryptContext
from app.security import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user_service(user, db):
    existing_user = db.query(User).filter(User.username == user.username).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username ya existe")
    
    hashed_password = pwd_context.hash(user.contraseña)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def login_user(form_data, db):
    db_user = db.query(User).filter(User.username == form_data.username).first()
    if not db_user: 
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
    if not pwd_context.verify(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}