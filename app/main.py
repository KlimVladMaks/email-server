from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from sqladmin import Admin
from . import models, schemas, crud
from .database import engine, get_db
from .admin import AdminAuth, UserAdmin

# Создаём таблицы в БД
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Добавляем поддержку сессий для всего приложения
app.add_middleware(SessionMiddleware, secret_key="secret-key")

# Создаём админ-панель (используем тот же секретный ключ)
admin = Admin(app, engine, authentication_backend=AdminAuth(secret_key="secret-key"))

# Регистрируем модели в админ-панели
admin.add_view(UserAdmin)

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

@app.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Вход пользователя с созданием сессии
    """
    # Авторизация пользователя
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль",
        )
    
    session = crud.create_session(db, user.id)

    return {
        "token": session.token,
        "type": "Bearer"
        }

@app.post("/logout")
async def logout(

):
    pass
