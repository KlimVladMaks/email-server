from sqlalchemy.orm import Session
from . import models, schemas, utils

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Если пользователь уже существует, возвращаем None
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        return None
    
    hashed_password = utils.hash_password(user.password)

    db_user = models.User(
        username=user.username,
        password=hashed_password,
        is_active=True
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def authenticate_user(db: Session, username: str, password: str):
    """Аутентификация пользователя"""
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not utils.verify_password(password, user.password):
        return False
    return user

def create_session(db: Session, user_id: int):
    """Создание новой сессии пользователя"""
    token = utils.generate_session_token()

    session = models.Session(
        token = token,
        user_id = user_id
    )

    db.add(session)
    db.commit()
    db.refresh(session)
    return session

def logout_session(db: Session, token: str):
    """Завершение сессии (logout)"""
    session = db.query(models.Session).filter(
        models.Session.token == token
    ).first()
