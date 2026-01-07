from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, crud
from .database import get_db

app = FastAPI()

@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Регистрация нового пользователя
    """
    db_user = crud.create_user(db, user)

    # Если пользователь уже существует
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким username уже существует"
        )

    return db_user

@app.get("/")
def read_root():
    """
    Тестовый endpoint для проверки работы API
    """
    return {"message": "API работает"}
