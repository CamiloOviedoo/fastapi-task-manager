# FastAPI Task Manager

## Descripción

FastAPI Task Manager es una API REST desarrollada con Python y FastAPI para gestionar tareas de usuarios.

Cada usuario puede registrarse, iniciar sesión mediante autenticación JWT y administrar únicamente sus propias tareas.

## Tecnologías utilizadas

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Pydantic
- Uvicorn

## Funcionalidades

- Registro de usuarios.
- Inicio de sesión con JWT.
- Obtener el usuario autenticado.
- Crear tareas.
- Listar tareas del usuario.
- Actualizar tareas.
- Eliminar tareas.
- Cada usuario solo puede acceder a sus propias tareas.

## Cómo ejecutar el proyecto

1. Clonar el repositorio.
2. Crear un entorno virtual.
3. Instalar las dependencias.
4. Configurar el archivo `.env`.
5. Ejecutar:

```bash
uvicorn app.main:app --reload
```

## Documentación

Una vez iniciado el servidor, la documentación está disponible en:

```
http://127.0.0.1:8000/docs
```