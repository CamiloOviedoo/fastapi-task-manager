from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, tasks

app = FastAPI(
    tittle="Users API",
    description="API de usuarios con fastAPI y arquitectura en capas",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(tasks.router)